#!/usr/bin/env python3

import sys

filename=sys.argv[1]

D=[]
with open(filename) as fp:
	for index, line in enumerate(fp):
		D.append(int(line.strip()))

p=-1
inc=0
for d in D:
	if p > 0 and d > p:
		inc+=1
	p=d
print(inc)
		
