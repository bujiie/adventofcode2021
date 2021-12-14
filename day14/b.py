#!/usr/bin/env python3

from sys import argv
from collections import defaultdict

T=None
P=defaultdict(str)
with open(argv[1]) as fp:
	for i, l in enumerate(fp):
		l=l.strip()
		if i == 0:
			T=l
		elif len(l) == 0:
			continue
		else:
			key, value = l.split(' -> ')
			P[key] = value

C = defaultdict(int)
for i in range(len(T)-1):
	key = T[i]+T[i+1]
	C[key] += 1

for _ in range(40):
	# list() forces the dict keys to a list that
	# python allows to change for each iteration.
	CC = defaultdict(int)
	for k in list(C):
		# BC -> BB (first_key), BC (second_key)
		first_key = k[0]+P[k]
		CC[first_key] += C[k]

		second_key = P[k]+k[1]
		CC[second_key] += C[k]
	C = CC
	print(C)
	print()

R = defaultdict(int)
for k in C:
	R[k[0]] += C[k]
R[T[-1]] += 1

print(max(R.values())-min(R.values()))


