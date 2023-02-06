#!/usr/bin/python3

def minOperations(n):
    """
    Returns the minimum number of operations needed to result in n H characters in the text file
    """
    # Edge case: if n is less than or equal to 0, return 0
    if n <= 0:
        return 0

    # Variable to store the count of operations
    operations = 0

    # Keep dividing n by 2 until it is greater than or equal to 1
    while n >= 1:
        # Check if n is even or odd
        if n % 2 == 0:
            # If n is even, divide n by 2
            n = n / 2
        else:
            # If n is odd, add 1 to it and divide by 2
            n = (n + 1) / 2
            operations += 1

    # Return the number of operations
    return operations

print(minOperations(12))