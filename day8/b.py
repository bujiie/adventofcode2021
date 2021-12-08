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

    
    print(N)
        
        
    




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
            
          
        

        
