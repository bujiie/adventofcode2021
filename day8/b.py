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


M={
    'abcdef': 0,
    'bc': 1,
    'abdeg': 2,
    'abcdg': 3,
    'bcfg': 4,
    'acdfg': 5,
    'acdefg': 6,
    'abc': 7,
    'abcdefg': 8,
    'abcdfg': 9
}
count=0
# figure out what the segment to letter mapping is...
for i in I:
    left,right=i
    zero,one,two,three,four,five,six,seven,eight,nine=None,None,None,None,None,None,None,None,None,None
    fives=[]
    sixes=[]
    N={}
    for l in left:
        ll=len(l)
        l=''.join(sorted(l))
        if ll==2:
            one=l
        elif ll==3:
            seven=l
        elif ll==4:
            four=l
        elif ll==7:
            eight=l
        elif ll==5:
            fives.append(l)
        else:
            sixes.append(l)

    a=seven
    for c in one:
        a=a.replace(c, '') 
    N['a']=a 

    for num in fives:
        if one[0] in num and one[1] in num:
            three=num
            for seg in num:
                if seg in four and seg not in one:
                    N['g']=seg
                    break 

    a=four
    for c in one:
        a=a.replace(c, '')
    a=a.replace(N['g'], '')
    N['f']=a

    for num in sixes:
        if N['g'] not in num:
            zero=num
        elif one[0] in num and one[1] in num:
            nine=num
        else:
            six=num

    for num in fives:
        if num == three:
            continue
        elif N['f'] in num:
            five=num
        else:
            two=num

    for seg in five:
        if seg in [N['g'],N['f'],N['a']]:
            continue
        elif seg in one:
            N['c']=seg
        else:
            N['d']=seg

    if one[0]==N['c']:
        N['b']=one[1]
    else:
        N['b']=one[0]

    for seg in two:
        if seg not in N.values():
            N['e']=seg

   
    N_i={v: k for k, v in N.items()} 
    nums=[]
    for r in right:
        rr=len(r) 
        r=''.join(sorted(r))
        if rr==2:
            nums.append(1) 
        elif rr==3:
            nums.append(7)
        elif rr==4:
            nums.append(4)
        elif rr==7:
            nums.append(8)
        else:
            key=""
            for c in r:
                key+=N_i[c]
            key=''.join(sorted(key))
            nums.append(M[key])

    multi=1
    result=0
    for n in reversed(nums):
        result+=(n*multi)
        multi*=10
    count+=result 
       

print(count)
            
          
        

        
