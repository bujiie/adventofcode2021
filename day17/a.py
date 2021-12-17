#!/usr/bin/env python3

from sys import argv
from collections import defaultdict
from math import sqrt, ceil, floor

# Assumes our input is in the same directory as this script and is named 'in'. 
# Otherwise it must be specified explicitly as a positional argument.
filename = argv[1] if len(argv) > 1 else 'in'

tx=[]
ty=[]
with open(filename) as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        pieces = line.split(' ')
        x, y = pieces[-2][2:-1], pieces[-1][2:]
        tx = [int(n) for n in x.split('..')]
        ty = [int(n) for n in y.split('..')]


my = 0
# can't be greater than tx[1] otherwise we'd
# overshoot on the second step.
for vx in range(tx[1]):
    for vy in range(-150, 500):
        x = 0
        y = 0
        lvx = vx
        lvy = vy
        lmax = 0
        found = False

        # some range of steps that you know will include
        # the target zone.
        for _ in range(300):
            x += lvx
            y += lvy
            lmax = max(lmax, y)
            lvy -= 1

            if lvx > 0:
                lvx -= 1
            elif lvx < 0:
                lvx += 1
            
            # check if position is in target area.
            if tx[0] <= x <= tx[1] and ty[0] <= y <= ty[1]:
                found = True
        if found:
            if lmax > my:
                my = lmax
print(my)

