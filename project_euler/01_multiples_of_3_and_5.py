#!/bin/python

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.

Input Format
First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Constraints
1 <= T <= 10^5
1 <= N <= 10^9

Output Format
For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.
'''

def arithmetic_series(n, N):
    '''Compute arithmetic series.'''
    return ((N / n) * (n + n * (N / n))) / 2

# Receive standard input (number of tests)
T = int(raw_input())

# Iterate through tests
for _ in range(T):
    
    # Receive standard input (end of sequence)
    N = int(raw_input()) - 1
    
    # Print sum
    print arithmetic_series(3, N) + arithmetic_series(5, N) - arithmetic_series(15, N)
