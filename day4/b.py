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
last_d=-1
latest_winning_board=-1
winners=[]

di=0
while len(winners) < len(boards):
	d=draw[di]
	last_d=d
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
					if b not in winners:
						winners.append(b)
					break
	di+=1

s=0
last_winner=winners[-1]
for x in boards[last_winner]:
	if boards[last_winner][x] not in M[last_winner]:
		s+=x

print(last_d*s)
