#!/bin/python

# Import modules
import sys
import math

# Receive standard input
guests, cookies = raw_input().strip().split(' ')
guests, cookies = [int(n), int(m)]

# If guests outnumber or equal cookies, bake the difference
if guests >= cookies:
    print guests - cookies
# Otherwise, find the difference to the nearest multiple and bake as many cookies
else:
    print int((math.ceil(cookies / float(n)) * guests) - cookies)
