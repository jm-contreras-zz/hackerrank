#!/bin/python

import sys
import math


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]

if n >= m:
    print n - m
else:
    print int((math.ceil(m / float(n)) * n) - m)
