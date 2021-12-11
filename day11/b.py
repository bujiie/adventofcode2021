#!/usr/bin/env python3

from sys import argv

L=[]
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        L.append([int(n) for n in l])

U=[]
xlen,ylen=len(L),len(L[0])

coords=[]
for x in range(xlen):
    for y in range(ylen):
        coords.append((x,y))

def pprint(m):
    for mm in m:
        print(''.join([str(n) for n in mm]))
    print()

flash_counts=[]

flashed=set()
steps=0
while len(flashed) < 100:
    visit=coords.copy()
    #print(f"step {i}")
    #pprint(L)
    flashed=set()
    while len(visit) > 0:
        x,y=visit.pop(0)

        if (x,y) in flashed:
            continue
        elif L[x][y]<9:
            L[x][y]+=1
        else:
            L[x][y]=0
            flashed.add((x,y))
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if dx==0 and dy==0:
                        continue
                    xx=x+dx
                    yy=y+dy
                    if 0 <= xx < xlen and 0 <= yy < ylen:
                        visit.append((xx,yy))
    steps+=1

print(steps)

                 
    



