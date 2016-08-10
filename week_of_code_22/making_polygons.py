#!/bin/python

'''
A polygon is a closed shape with three or more sides. For example, triangles are polygons. A polygon is non-degenerate if it has no
overlapping sides (and no sides of zero length).

You have n sticks with positive integer lengths, a0, a1, ..., an-1. You want to create a polygon using all n sticks. Because this is
not always possible, you can cut one or more sticks into two smaller sticks (they do not necessarily need to be of integer length) and
repeat the process of trying to create a polygon using all the sticks. Given the lengths of all n sticks, find and print the minimum
number of cuts necessary to make a non-degenerate polygon.

Input Format
The first line contains a single integer, n. 
The second line contains  space-separated integers describing the respective values of a0, a1, ..., an-1.

Constraints
1 <= n <= 50
1 <= ai <= 100

Output Format
Print a single integer denoting the minimum number of cuts required to make the n sticks into a polygon.
'''

# Import module
import sys

# Receive standard input
n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

# Fewer than 3 sticks
if n < 3:
    # Make 1 cut for each missing side of a triangle
    print 3 - n
    
# 3 or more sticks
else:
    # Count of sticks that meet triangle inequality condition
    count = 0
    # Iterate through sticks
    for i, i_stick in enumerate(a):
        # Add to count if condition met
        if i_stick < sum(a) / float(2):
            count += 1
    # Make cut if not all sticks meet condition
    print int(count != n)
