#!/bin/python

'''
You're having a cookie party tonight! You're expecting n guests and you've already made m cookies. You want to distribute all the
cookies evenly between your guests in such a way that each guest receives the same number of whole cookies. If there are not enough
cookies to give everyone the same amount, you must make some number of additional cookies.

Given n and m, find and print the minimum number of additional cookies you must make so that everybody receives the same number of
cookies.

Input Format
A single line of two space-separated integers describing the respective values of n and m.

Constraints
1 <= n, m <= 10^9

Output Format
Print a single integer denoting the number of additional cookies you need to make so that everyone at the cookie party has the same
number of whole cookies.
'''

# Import modules
import sys
import math

# Receive standard input
n, m = raw_input().strip().split(' ')
guests, cookies = [int(n), int(m)]

# If guests outnumber or equal cookies, bake the difference
if guests >= cookies:
    print guests - cookies
# Otherwise, find the difference to the nearest multiple and bake as many cookies
else:
    print int((math.ceil(cookies / float(n)) * guests) - cookies)
