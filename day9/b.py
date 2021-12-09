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
            lspots.append((xi, yi, target))

B=[]
for spot in lspots:
    visit={spot}
    b={spot}
    while len(visit) > 0:
        x,y,c=visit.pop()
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx==dy or (dx==0 and dy==0) or dx==-dy:
                    continue
                xx=x+dx
                yy=y+dy
                if 0 <= xx < xlen and 0 <= yy < ylen:
                    s=M[xx][yy]
                    if s > c and s!=9 and s not in b:
                        coord=(xx,yy,s)
                        visit.add(coord)
                        b.add(coord)
    B.append(b)


B_size=sorted(list(map(lambda x: len(x), B)), reverse=True)
result=1
for i in range(3):
    result*=B_size[i]     
print(result) 
