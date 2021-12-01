#!/usr/bin/env python3

import sys

filename=sys.argv[1]

with open(filename) as fp:
	for index, line in enumerate(fp):
		line = line.strip()
		print(line)
