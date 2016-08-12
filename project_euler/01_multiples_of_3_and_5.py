# Receive standard input (number of test cases)
T = int(raw_input())

# Iterate through integers
for _ in xrange(T):

    # Receive standard input (end of sequence)
    N = int(raw_input())
    
    # Return sum
    print sum([i for i in range(1, N) if i % 3 == 0 or i % 5 == 0])
