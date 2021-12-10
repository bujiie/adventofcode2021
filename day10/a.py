#!/usr/bin/env python3

from sys import argv


L=[]
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()

        L.append([c for c in l])

closing={
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
 
illegal=[]
for line in L:
    stack=[]
    for c in line:
        if c in ['(','[','{','<']:
            stack.append(c)
        else:
            top=stack.pop()
            if top != closing[c]: 
                illegal.append(c)
                break

scores={
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

result=0
for i in illegal:
    if i not in scores:
        print(f"{i} not in score")
    else:
        result+=scores[i]

print(result)
                        
     
