#!/usr/bin/env python3

from sys import argv


M=[]
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        M.append([int(n) for n in l])

xlen=len(M)
ylen=len(M[0])
lspots=[]
for xi, x in enumerate(M):
    for yi, y in enumerate(x):
        target=M[xi][yi] 
        ok=True
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx==dy or (dx==0 and dy == 0):
                    continue
                xx=xi+dx
                yy=yi+dy
                if 0 <= xx < xlen and 0 <= yy < ylen:
                    if M[xx][yy] <= target:
                        ok=False
                        break
            if not ok:
                break
        if ok:
            lspots.append(target)

result=0
for spot in lspots:       
    result+=(spot+1)

print(result)
    
