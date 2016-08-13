# Receive standard input (number of tests)
T = int(raw_input())

# Iterate through tests
for _ in range(T):
    
    # Receive standard input (maximum number)
    N = int(raw_input())
    
    # Initialize Fibonacci sequence
    F = [1, 2]
    
    # Compute next number to add
    next_f = F[-1] + F[-2]
    
    # Iterate while number is smaller than N
    while next_f < N:
        
        # Append next number
        F.append(next_f)
        
        # Compute the next one
        next_f = F[-1] + F[-2]
    
    # Report sum of even numbers
    print sum([f for f in F if f % 2 == 0])
