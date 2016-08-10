#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

if n == 1:
    print 2
elif n == 2:
    print 1
else:
    x = 0
    for i, this_a in enumerate(a):
        if this_a < sum(a) / float(2):
            x += 1
    if x == n:
        print 0
    else:
        print 1
