#!/usr/bin/env python3

from sys import argv

M={}
L=[]
c=0
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()
        L.append(l)
        for j,b in enumerate(l):
            if j not in M:
                M[j]=0

            if int(b)==1:
                M[j]+=1
        c+=1

D=L
H=[]
i=0
while len(D) > 1:
    q=[0,0]
    for d in D:
        if d[i] == '1':
            q[1]+=1
        else:
            q[0]+=1

    k=''
    if q[1] >= q[0]:
        k='1'
    else:
        k='0'
    
    for d in D:
        if d[i] == k:
            H.append(d)
    D=H
    H=[]
    i+=1 

W=L
Y=[]
j=0
while len(W) > 1:
    q=[0,0]
    for w in W:
        if w[j] == '1':
            q[1]+=1
        else:
            q[0]+=1

    k=''
    if q[1] < q[0]:
        k='1'
    else:
        k='0'
    
    for w in W:
        if w[j] == k:
            Y.append(w)
    W=Y
    Y=[]
    j+=1 

print(int(D[0],2)*int(W[0],2))

