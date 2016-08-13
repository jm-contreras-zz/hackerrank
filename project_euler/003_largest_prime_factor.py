#!/bin/python

'''
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of a given number N?

Input Format
First line contains T, the number of test cases. This is followed by T lines each containing an integer N.

Output Format 
For each test case, display the largest prime factor of N.

Constraints
1 <= T <= 10
10 <= N <= 10^12
''' 

# Receive standard input (number of test cases)
T = int(raw_input())

# Iterate through test cases
for _ in range(T):
    
    # Receive standard input (top number)
    N = int(raw_input())
    
    # Start with 2 and continue until its square is larger than N
    x = 2
    while x * x <= N:
        
        # If divisble, add 1
        if N % x:
            x += 1
        
        # Otherwise, divide by x
        else:
            N /= x
    
    # If N remains larger than 1, return it
    if N > 1:
        print N
    
    # Otherwise, return x
    else:
        print x
        
