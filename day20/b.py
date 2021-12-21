#!/usr/bin/env python3

from sys import argv
from collections import defaultdict

# Assumes our input is in the same directory as this script and is named 'in'.
# Otherwise it must be specified explicitly as a positional argument.
filename = argv[1] if len(argv) > 1 else 'in'

algo = ''
lights = []
L = set()
l_count = 0
flag = False
with open(filename) as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        if len(line) == 0:
            flag = True
            continue
        if not flag:
            algo += line
        else:
            lights.append(list(line))
            for j, v in enumerate(line):
                if v == '#':
                    L.add((l_count,j))
            l_count += 1

for i in range(50):
    xlo, xhi = min([x for x, _ in L]), max([x for x, _ in L])
    ylo, yhi = min([y for _, y in L]), max([y for _, y in L])
    on = (i%2 == 0)
    LL = set()
    for x in range(xlo-5, xhi+5):
        for y in range(ylo-5, yhi+5):
            word = ''
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    xx = x + dx
                    yy = y + dy
                    if ((xx, yy) in L) == on:
                        word += '1'
                    else:
                        word += '0'
            n = int(f"0b{word}", 2)
            if (algo[n] == '#') != on:
                LL.add((x, y))
    L = LL

print(len(L))






