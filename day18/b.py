#!/usr/bin/env python3

from sys import argv, setrecursionlimit
from collections import defaultdict
from functools import reduce
from itertools import permutations

# Assumes our input is in the same directory as this script and is named 'in'. 
# Otherwise it must be specified explicitly as a positional argument.
filename = argv[1] if len(argv) > 1 else 'in'


def magnitude(node):
    if isinstance(node, int):
        return node
    return 3*magnitude(node[0]) + 2*magnitude(node[1])

# assume that nothing is nested further than 4 levels deep.
# (left, right), value, has_exploded
def explode(node, n = 4):
    if isinstance(node, int):
        return (None, None), node, False
    if n == 0:
        return tuple(node), 0, True
    left, right = node
    (l, r), left, has_exploded = explode(left, n-1)
    if has_exploded:
        return (l, None), [left, add_left(right, r)], True
    (l, r), right, has_exploded = explode(right, n-1)
    if has_exploded:
        return (None, r), [add_right(left, l), right], True
    return (None, None), node, False

def add_left(node, n):
    if n is None:
        return node
    if isinstance(node, int):
        return node + n
    return [add_left(node[0], n), node[1]]

def add_right(node, n):
    if n is None:
        return node
    if isinstance(node, int):
        return node + n
    return [node[0], add_right(node[1], n)]

def add(a, b):
    node = [a, b]
    while True:
        _, node, has_changed = explode(node)
        if has_changed:
            continue
        node, split_done = split(node)
        if not split_done:
            break
    return node

def split(node):
    if isinstance(node, int):
        if node >= 10:
            a = node // 2
            b = node - a
            return [a, b], True # split is done
        return node, False # split is not done
    left, right = node
    left, split_done = split(left)
    if split_done:
        return [left, right], True
    right, split_done = split(right)
    return [left, right], split_done

P = []
with open(filename) as fp:
    P = list(map(eval, fp.read().splitlines()))

print(max(magnitude(add(l, r)) for l, r in permutations(P, 2)))

