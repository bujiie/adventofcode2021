#!/usr/bin/env python3

from sys import argv
from collections import defaultdict

template=None
P=defaultdict(str)
with open(argv[1]) as fp:
	for i, l in enumerate(fp):
		l=l.strip()
		if i == 0:
			template=l
		elif len(l) == 0:
			continue
		else:
			key, value = l.split(' -> ')
			P[key] = value

res = ''
for _ in range(10):
	res = template[0]
	for i in range(1, len(template)):	
		key = template[i-1]+template[i]
		if key in P:
			res += P[key]+template[i]
	template = res

C=defaultdict(int)
for c in template:
	C[c] += 1

mx, mn = max(C.values()), min(C.values())
	
print(mx-mn)


