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


# figure out what the segment to letter mapping is...





# update this map with the mappings
M={
    'abcdeg': 0,
    'acdfgc': 2,
    'abcdf': 3,
    'bcdef': 5,
    'bcdefg': 6,
    'abcdef': 9
}
count=0
for i in I:
    _,r=i
    nums=[]
    for rr in r:
        l=len(rr)
        if l==2:
            nums.append(1)
        elif l==3:
            nums.append(7)
        elif l==4:
            nums.append(4)
        elif l==7:
            nums.append(8)
        else:
            sorted_rr=''.join(sorted(rr))
            nums.append(M[sorted_rr])
    multi=1
    result=0
    for n in nums:
        result+=(n*multi)
        multi*=10
    count+=result 
            
        

print(count)
            
          
        

        
