#!/usr/bin/env python3

from sys import argv


F=None
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        F=[int(n) for n in l.split(',')]

M={}
for f in F:
    if f not in M:
        M[f]=0
    M[f]+=1

days=80

C={}
for d in range(0, days):
    for f in M:
        if f not in C:
            C[f]=[f]
        F_new=[]
        for fi, ff in enumerate(C[f]):
            if ff==0:
                C[f][fi]=6
                F_new.append(8)
            else:
                C[f][fi]-=1
        C[f]=C[f]+F_new 
   
count=0  
for m in M:
    count+=(M[m]*len(C[m]))         
print(count)
            
