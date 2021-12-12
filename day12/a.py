#!/usr/bin/env python3

from sys import argv
import re

S={}
with open(argv[1]) as fp:
	for i, l in enumerate(fp):
		l=l.strip()
		s,e=l.split('-')
		if s == 'end' or e == 'start':
			s,e=e,s
			
		if s not in S:
			S[s]=[]
		S[s].append(e)
		if s not in ['start','end'] and e not in ['start','end']:
			if e not in S:
				S[e]=[]
			S[e].append(s)

lower_regex=r"[a-z]+"
upper_regex=r"[A-Z]+"

def process(nodes=[], path=[], visited=[], acc=[]):
	for node in nodes:
		local_visited=visited.copy()
		local_path=path.copy()
		if node == 'end':
			# path is complete.
			local_path.append(node)
			acc.append(local_path)
			continue
		elif node not in S:
			continue
		else:
			# path is not complete.
			if re.match(lower_regex, node):
				if node in local_visited:
					continue
				else:
					local_path.append(node)
					local_visited.append(node)
			else:
				local_path.append(node)
			process(S[node], local_path, local_visited, acc)
	
paths=[]	
process(S['start'], ['start'], [], paths)
print(len(paths))
