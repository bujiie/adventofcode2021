#!/usr/bin/env python3

from sys import argv
from collections import defaultdict

# Assumes our input is in the same directory as this script and is named 'in'. 
# Otherwise it must be specified explicitly as a positional argument.
filename = argv[1] if len(argv) > 1 else 'in'

p = []
with open(filename) as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        s = line.split(' ')
        p.append((int(s[1]), int(s[-1])))

def move(start, steps):
    remainder = (start + steps) % 10
    return 10 if remainder == 0 else remainder

def roll_generator(n_rolls = 3, rollover = 100):
    i = 1
    count = 0
    total = 0
    while True:
        total += i
        count += 1
        if count == n_rolls:
            yield total
            count = 0
            total = 0
        if i == rollover:
            i = 1
        else:
            i += 1

roll = roll_generator()

# (position, score)
player1 = (p[0][1], 0)
player2 = (p[1][1], 0)

i = 0
while player1[1] < 1000 and player2[1] < 1000:
    rolls = next(roll)
    if i % 2 == 0: # player 1
        pos = move(player1[0], rolls)
        player1 = (pos, player1[1] + pos)
    else: # player 2
        pos = move(player2[0], rolls)
        player2 = (pos, player2[1] + pos)
    i += 1

print(3 * i * min(score for _, score in [player1, player2]))
