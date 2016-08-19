# Receive standard input (number of tests)
T = int(raw_input())

# Create empty list of palindromes
palindromes = []

# Create iterator of 3-digit numbers
three_digit_nums = range(999, 99, -1)

# Iterate through every digit combination,
# storing their product
for i in three_digit_nums:
    for j in three_digit_nums:
        product = str(i * j)
        # If it is a palindrome, store it in the list
        if product == product[::-1]:
            palindromes.append(int(product))

# Sort the list in descending order
palindrome_list.sort(reverse=True)

# Iterate through test cases, receiving standard input
for _ in range(T):
    N = int(raw_input())
    # Iterate through numbers in palindrome and print
    # the largest one smaller than N, then break
    for p in palindromes:
        if p < N:
            print p
            break
        
