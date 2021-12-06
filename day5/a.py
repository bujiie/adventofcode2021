#!/usr/bin/env python3

from sys import argv


P={}
with open(argv[1]) as fp:
	for i, l in enumerate(fp):
		l=l.strip()
		s,e=l.split(' -> ')
		x1,y1=tuple([int(n) for n in s.split(',')])
		x2,y2=tuple([int(n) for n in e.split(',')])
	
		x1,x2=min(x1,x2),max(x1,x2)
		y1,y2=min(y1,y2),max(y1,y2)

		if x1==x2 or y1==y2:
			for x in range(x1, x2+1):
				for y in range(y1, y2+1):
					if (x,y) not in P:
						P[(x,y)]=0
					P[(x,y)]+=1


count=0
for p in P:
	if P[p] > 1:
		count+=1

print(count)

				

