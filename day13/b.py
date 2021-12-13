#!/usr/bin/env python3

from sys import argv


dots=set()
folds=[]
last_y_fold=None
last_x_fold=None
with open(argv[1]) as fp:
	for i, l in enumerate(fp):
		l=l.strip()
		if l.startswith('fold'):
			plane,line=l.split(' ')[-1].split('=')
			line=int(line)
			folds.append((plane, line))
			if plane == 'y' and (last_y_fold is None or line < last_y_fold):
				last_y_fold=line
			if plane == 'x' and (last_x_fold is None or line < last_x_fold):
				last_x_fold=line

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
		if x > fold_on:
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

for y in range(last_y_fold):
	for x in range(last_x_fold):
		if (x,y) in res:
			print('#', end='')
		else:
			print('.', end='')
	print()
