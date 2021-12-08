#!/usr/bin/env python3

from sys import argv


with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        print(l)
