#!/bin/python

'''
Consider two -element sets of integers which may contain duplicate numbers,  and . You can perform the following operation on set :

Choose two elements at some postions  and  where .
Decrement  by  and increment  by .
Given  and , find and print the minimum number of operations you must perform so that  is equal to  (i.e., both sets contain the same exact values, and the order doesn't matter); if such a thing is not possible, print instead.

Input Format

The first line contains a single integer, . 
The second line contains  space-separated integers describing the respective values of set . 
The third line contains  space-separated integers describing the respective values of set .

Constraints
, where .
 for at least  of the test cases.
Output Format

Print a single integer denoting the minimum number of operations required to make set X equal to set Y; if no number of operations will
ever make the two sets equal, print -1 instead.
'''

# Read standard input
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
