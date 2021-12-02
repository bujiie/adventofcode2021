#!/usr/bin/env python3

from sys import argv

x=0
y=0

with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        (d, delta) = l.split(" ")
        delta=int(delta)
        if d == "forward":
            x+=delta
        if d == "down":
            y+=delta
        if d == "up":
            y-=delta

print(x*y)
         
