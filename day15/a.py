#!/usr/bin/env python3

from sys import argv
from collections import defaultdict
import heapq

R=[]
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        R.append([int(n) for n in l])

rlen = len(R)
clen = len(R[0])
visited = set()

def dijkstra(grid):
    heep = [(0, (0,0))]
    while heep:
        cost, (r,c) = heapq.heappop(heep)
        if (r,c) in visited:
            continue
        visited.add((r,c))
        if (r,c) == (rlen-1, clen-1):
            return cost
    
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dc == dr or dc == -dr:
                    continue
                rr = r + dr 
                cc = c + dc
                if 0 <= rr < rlen and 0 <= cc < clen:
                    new_cost = grid[rr][cc] + cost
                    heapq.heappush(heep, (new_cost, (rr,cc)))

print(dijkstra(R)) 
                
        
        
