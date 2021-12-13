#!/usr/bin/env python3

from sys import argv


dots=set()
folds=[]
with open(argv[1]) as fp:
	for i, l in enumerate(fp):
		l=l.strip()
		if l.startswith('fold'):
			plane,line=l.split(' ')[-1].split('=')
			folds.append((plane, int(line)))
		elif len(l) == 0:
			continue
		else:
			dots.add(tuple([int(n) for n in l.split(',')]))

def fold_y(fold_on, dots=set()):
	ylen=fold_on*2
	new_dots=set()

	for dot in dots:
		x,y=dot
		if y > fold_on:
			new_dots.add((x, ylen-y))
		else:
			new_dots.add(dot)
	return new_dots	

def fold_x(fold_on, dots=set()):
	xlen=fold_on*2
	new_dots=set()

	for dot in dots:
		x,y=dot
		if x < fold_on:
			new_dots.add((xlen-x, y))
		else:
			new_dots.add(dot)
	return new_dots

res=dots
for fold in folds:
	plane,line=fold
	if plane == 'x':
		res=fold_x(line, res)
	else:
		res=fold_y(line, res)


print(len(res))
