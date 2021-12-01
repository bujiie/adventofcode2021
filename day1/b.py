#!/usr/bin/env python3

import sys

filename=sys.argv[1]

D=[]
with open(filename) as fp:
	for index, line in enumerate(fp):
		D.append(int(line.strip()))

p=-1
inc=0
for i,d in enumerate(D):
	if i > len(D)-3:
		break
	s=0
	for j in [0, 1, 2]:
		s+=D[i+j]
	
	if p > 0 and s > p:
		inc+=1
	p=s
print(inc)
		
