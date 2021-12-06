#!/usr/bin/env python3

from sys import argv
from collections import defaultdict


F=None
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        F=[int(n) for n in l.split(',')]

M=defaultdict(int)
for f in F:
    if f not in M:
        M[f]=0
    M[f]+=1


for d in range(256):
    N=defaultdict(int)
    for i,v in M.items():
        if i==0:
            N[6]+=v
            N[8]+=v
        else:
            N[i-1]+=v
    M=N

print(sum(M.values()))
            
