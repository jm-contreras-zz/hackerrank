#!/bin/python

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
