#!/usr/bin/env python3

from sys import argv
from collections import defaultdict
from itertools import product

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

G = {}

game_limit = 21
def play(p1, s1, p2, s2):
    if s1 >= game_limit:
        return (1, 0)
    if s2 >= game_limit:
        return (0, 1)

    if (p1, s1, p2, s2) in G:
        return G[(p1, s1, p2, s2)]

    scores = (0, 0)
    for r in product([1,2,3], repeat=3):
        np1 = move(p1, sum(r))
        ns1 = s1 + np1
        ss1, ss2 = play(p2, s2, np1, ns1)
        scores = (scores[0] + ss2, scores[1] + ss1)
    G[(p1, s1, p2, s2)] = scores
    return scores


print(max(play(player1[0], player1[1], player2[0], player2[1])))


