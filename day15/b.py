#!/usr/bin/env python3

from sys import argv
from collections import defaultdict
import heapq

R=[]
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        R.append([int(n) for n in l])

visited = set()

def dijkstra(grid):
    rlen = len(grid)
    clen = len(grid[0])

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


def expand_grid(grid, multiplier=5):
    rlen = len(grid)
    clen = len(grid[0])
    cols = clen*multiplier
    rows = rlen*multiplier

    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        mr = r // rlen
        for c in range(cols):
            mc = c // clen
            rel_r = r if r < rlen else r % rlen
            rel_c = c if c < clen else c % clen
            ans = grid[rel_r][rel_c] + mr + mc
            ans = ans if ans <= 9 else ans % 9
            new_grid[r][c] = ans
    return new_grid

ER = expand_grid(R)
print(dijkstra(ER)) 
                
        
        
