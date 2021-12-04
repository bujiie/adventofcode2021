#!/usr/bin/env python3

from sys import argv

draw=[]
boards={}
b=-1
br=0
with open(argv[1]) as fp:
	for i, l in enumerate(fp):
		l=l.strip()
		if i == 0:
			draw=[int(n) for n in l.split(',')]
			continue
		if len(l) != 0:
			for pi, p in enumerate(l.split()):
				boards[b][int(p)]=(br,pi)
			br+=1
		else:
			b+=1
			br=0
			boards[b]={}

M={}
bingo=False
last_d=-1
for d in draw:
	for bi, b in enumerate(boards):
		if d in boards[b]:
			if bi not in M:
				M[bi]=[]
			M[bi].append(boards[b][d])
			
			c=([[],[],[],[],[]],[[],[],[],[],[]])
			for m in M[bi]:
				x,y=m
				c[0][x].append(m)
				c[1][y].append(m)

				if len(c[0][x]) >= 5 or len(c[1][y]) >= 5:
					bingo=True
					break
		if bingo:
			s=0
			for x in boards[b]:
				if boards[b][x] not in M[bi]:
					s+=x
			print(d*s)
			break
	if bingo:
		break
