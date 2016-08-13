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
        
