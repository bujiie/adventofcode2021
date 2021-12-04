#!/usr/bin/env python3

import sys

filename=sys.argv[1]

p=None
i=0
with open(filename) as fp:
	for index, line in enumerate(fp):
		n=int(line.strip())
		if p is not None and n > p:
			i+=1
		p=n
print(i)


