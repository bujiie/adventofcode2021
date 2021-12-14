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

def fold(fold_on, dots=set()):
	axis,fold_line=fold_on
	# assumes we always fold exactly in half
	b4_fold_len=fold_line*2

	new_dots=set()
	for dot in dots:
		x,y = dot
		if axis == 'x':
			coord,folded_coord_pair=x,(b4_fold_len-x, y)
		else:
			coord,folded_coord_pair=y,(x, b4_fold_len-y)

		if coord > fold_line:
			new_dots.add(folded_coord_pair)
		else:
			new_dots.add(dot)
	return new_dots	

res=dots
last_folds={}
for f in folds:
	axis,fold_line=f
	last_folds[axis]=fold_line
	res=fold(f, res)

for y in range(last_folds['y']):
	for x in range(last_folds['x']):
		if (x,y) in res:
			print('#', end='')
		else:
			print(' ', end='')
	print()
