#!/bin/python

'''
Consider two -element sets of integers which may contain duplicate numbers, X = {x0, x1, ..., xn-1} and Y = {y0, y1, ..., yn-1}. You
can perform the following operation on set X:

1. Choose two elements at some postions xi and xj where 0 <= i < j < n.
2. Decrement xi by 1 and increment xj by 1.
Given X and Y, find and print the minimum number of operations you must perform so that X is equal to Y (i.e., both sets contain the
same exact values, and the order doesn't matter); if such a thing is not possible, print -1 instead.

Input Format
The first line contains a single integer, n. 
The second line contains n space-separated integers describing the respective values of set X. 
The third line contains n space-separated integers describing the respective values of set Y.

Constraints
1 <= n <= 10^5
-10^9 <= xi, yi <= 10^9, where 0 <= i < n.
n <= 50 for at least 50% of the test cases.

Output Format
Print a single integer denoting the minimum number of operations required to make set X equal to set Y; if no number of operations will
ever make the two sets equal, print -1 instead.
'''

# Receive standard input
n = int(raw_input())
X = [int(i) for i in raw_input().split(' ')]
Y = [int(i) for i in raw_input().split(' ')]

# Sort arrays
X.sort()
Y.sort()

# Compute differences
Z = [x - y for x, y in zip(X, Y)]

# If sum of differences is non-zero, then unsolvable
if sum(Z) != 0:
    print -1
# Otherwise, halve sum of absolute differences
else:
    print sum([abs(z) for z in Z]) / 2
