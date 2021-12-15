#!/usr/bin/env python3

from sys import argv
from collections import defaultdict

# Assumes our input is in the same directory as this script and is named 'in'. 
# Otherwise it must be specified explicitly as a positional argument.
filename = argv[1] if len(argv) > 1 else 'in'

with open(filename) as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        print(line)


