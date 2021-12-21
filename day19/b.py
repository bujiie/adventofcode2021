#!/usr/bin/env python3

from sys import argv
from collections import deque
from itertools import permutations, product
import numpy as np

# Assumes our input is in the same directory as this script and is named 'in'.
# Otherwise it must be specified explicitly as a positional argument.
filename = argv[1] if len(argv) > 1 else 'in'

B = {}
scanner = None
with open(filename) as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        if '---' in line:
            scanner = int(line.split(' ')[-2])
            B[scanner] = []
        elif len(line) > 0:
            B[scanner].append(tuple([int(n) for n in line.split(',')]))

def m_multiply(a, b):
    result = []
    for i in range(len(a)):
        row = []
        # iterate through columns of Y
        for j in range(len(b[0])):
            value = 0
            # iterate through rows of Y
            for k in range(len(b)):
                value += a[i][k] * b[k][j]
            row.append(value)
        result.append(row)
    return result

# 90 degree rotations in positive direction
rot_x = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
rot_y = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]
rot_z = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]

def rotate(point, r_matrix, degrees = 90):
    n = degrees // 90
    result = point
    for _ in range(n):
        result = m_multiply(r_matrix, result)
    return result

def rotate_x(point, degrees = 90):
    return rotate(point, rot_x, degrees)

def rotate_y(point, degrees = 90):
    return rotate(point, rot_y, degrees)

def rotate_z(point, degrees = 90):
    return rotate(point, rot_z, degrees)

# since everything is in increments of 90deg, we don't have to do
# real trig. we can just use a lookup table since everything is
# either 1, -1 or 0.
trig = {
    0: { 'sin': 0, 'cos': 1 },
    90: { 'sin': 1, 'cos': 0 },
    180: { 'sin': 0, 'cos': -1 },
    270: { 'sin': -1, 'cos': 0 }
}

def rot_matrix(vect):
    x,y,z = vect
    sinx, cosx = trig[x]['sin'], trig[x]['cos']
    siny, cosy = trig[y]['sin'], trig[y]['cos']
    sinz, cosz = trig[z]['sin'], trig[z]['cos']
    return np.array([
        [cosz*cosy, cosz*siny*sinx-sinz*cosx, cosz*siny*cosx+sinz*sinx],
        [sinz*cosy, sinz*siny*sinx+cosz*cosx, sinz*siny*cosx-cosz*sinx],
        [-siny, cosy*sinx, cosy*cosx]
    ])


# Because the absolute positions are not known, we cannot compare (x,y,z)
# points. Instead we use the distance between the beacons as the beacon
# orientation signature that can be compared.
def manhattan_distance(beacon1, beacon2):
    return sum(abs(point1 - point2) for point1, point2 in zip(beacon1, beacon2))

# Calculate a unique set of manhattan distances for the beacons around a scanner
# relative to each other. (b1, b2, distance)
def calc_manhattan_distances_for_scanner(scanner):
    return {(b1, b2, manhattan_distance(b1, b2)) for b2 in scanner for b1 in scanner}

def calc_manhattan_distances_for_scanners(scanners = {}):
    return {i: calc_manhattan_distances_for_scanner(scanner) for (i, scanner) in scanners.items()}

# memoize all the rotation matrix permutations so we don't have to keep
# calculating them for every point.
r_matrices = {}
for permute in product([0, 90, 180, 270], repeat=3):
    r_matrices[permute] = rot_matrix(permute)

def align(s1, s2):
    matches = [(b1, b2) for b1 in s1 for b2 in s2
               if len({manhattan_distance(b1, b) for b in s1} & {manhattan_distance(b2, b) for b in s2}) >= 12]

    if len(matches) == 0:
        return False

    target_r_matrix = None
    for i in r_matrices:
        r_matrix = r_matrices[i]
        l = set()
        for beacon1, beacon2 in matches:
            l.add(tuple(beacon1 - beacon2 @ r_matrix))
        if len(l) == 1:
            target_r_matrix = r_matrix
            break
    if target_r_matrix is not None:
        scanner_pos = matches[0][0] - matches[0][1] @ target_r_matrix
        return [tuple((s @ target_r_matrix )+ scanner_pos) for s in s2], scanner_pos


aligned_scanners = [B[0]]
unaligned_scanners = deque(list(B.values())[1:])
scanners_pos = [(0,0,0)]
while len(unaligned_scanners):
    candidate = unaligned_scanners.popleft()
    for ref in aligned_scanners:
        result = align(ref, candidate)
        if result:
            aligned_scanners += [result[0]]
            scanners_pos += [result[1]]
            break
    if not result:
        unaligned_scanners.append(candidate)

print(max(manhattan_distance(s1,s2) for s1 in scanners_pos for s2 in scanners_pos))
