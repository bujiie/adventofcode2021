#!/usr/bin/env python3

from sys import argv


L=[]
with open(argv[1]) as fp:
    for i, l in enumerate(fp):
        l=l.strip()

        L.append([c for c in l])

opening={
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
 
legal=[]
for line in L:
    stack=[]
    illegal=False
    for c in line:
        if c in ['(','[','{','<']:
            stack.append(c)
        else:
            top=stack.pop()
            if top != opening[c]: 
                illegal=True
                break
    if not illegal:
        legal.append(line)

closing={
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
   
completions=[]                    
for line in legal:
    stack=[]
    corrections=[]
    for c in line:
        if c in ['(','[','{','<']:
            stack.append(c)
        else:
            if len(stack) > 0:
                last=stack[-1]
                if last==opening[c]:
                    stack.pop()
    completions.append([closing[c] for c in reversed(stack)])

scores={
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

total_scores=[]
for comp in completions:
    result=0
    for c in comp:
        result*=5
        result+=scores[c]
    total_scores.append(result)

sorted_scores=sorted(total_scores)
print(sorted_scores[(len(sorted_scores)-1)//2])
