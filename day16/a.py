#!/usr/bin/env python3

from sys import argv
from collections import defaultdict

# Assumes our input is in the same directory as this script and is named 'in'. 
# Otherwise it must be specified explicitly as a positional argument.
filename = argv[1] if len(argv) > 1 else 'in'

M = defaultdict(str)
S = ''
with open(filename) as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        for c in line:
            if c not in M:
                M[c] = '{0:04b}'.format(int(c, base=16))
            S += M[c]

def bins_to_int(s):
    return int(f"0b{s}", 2)

def parse(subject, n_packets = None):
    mem = []
    count = 0
    while len(subject) > 0:
        if n_packets is not None and count >= n_packets:
            break

        # most likely padding because there is not enough bits for the headers.
        if len(subject) < 6:
            break

        ver, typ = bins_to_int(subject[:3]), bins_to_int(subject[3:6])

        subject = subject[6:]

        if len(subject) < 5:
            break
        #print(f"ver: {ver}, type: {typ}, subject: {subject}")
        if typ == 4:
            buff = ''            
            while True:
                ctrl, data = subject[0], subject[1:5]
                buff += data
                subject = subject[5:]
                if ctrl == '0':
                    break
            n = bins_to_int(buff)
            mem.append((ver, typ, n))
        else:
            mem.append((ver, typ, -1))
            length, subject = subject[0], subject[1:]
            if length == '0':
                n, subject = bins_to_int(subject[:15]), subject[15:]
                m, s = parse(subject[:n])
                mem += m
                subject = subject[n:]
            else:
                n, subject = bins_to_int(subject[:11]), subject[11:]
                m, s = parse(subject, n)
                mem += m
                subject = s
        count += 1
    return (mem, subject)

mem, s = parse(S)  
res = 0
for m in mem:
    ver, _, _ = m
    res += ver
print(res)

            
        


