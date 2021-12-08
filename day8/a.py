#!/usr/bin/env python3

from sys import argv


I=[]
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        left,right=l.split(' | ')
        lp=left.split(' ')
        rp=right.split(' ')
        I.append((lp,rp))


count=0
for i in I:
    _,r=i
    for rr in r:
        if len(rr) in [2,3,4,7]:
            count+=1

print(count)
            
          
        

        
