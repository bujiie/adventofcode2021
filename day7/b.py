#!/usr/bin/env python3

from sys import argv


P=[]
limits=None
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        P=[int(n) for n in l.split(',')]
        limits=(min(P),max(P))

least_fuel=None

S={}
for i in range(limits[1]+1):
    fuel=0
    for p in P:
        steps=abs(p-i)
        if steps not in S:
            S[steps]=sum(range(steps+1))
        fuel+=S[steps]
    if least_fuel is None or fuel < least_fuel:
        least_fuel=fuel

print(least_fuel)

