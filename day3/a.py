#!/usr/bin/env python3

from sys import argv

M={}
c=0
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        
        for j,b in enumerate(l):
            if j not in M:
                M[j]=0

            if int(b)==1:
                M[j]+=1
        c+=1

g=''
e=''
for k in M.keys():
    v=M[k]
    if v >= (c-v):
        g+='1'
        e+='0'
    else:
        g+='0'
        e+='1'    

print(int(g,2)*int(e,2))
        
