#!/usr/bin/python3
import sys
"""""
Function Description:
        Calculates the factorial of a non-negative integer using recursion.
        The factorial of n (n!) is the product of all positive integers less than or equal to n.
        By definition, 0! = 1.

    Parameters:
        n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
        int: The factorial of the input integer n.
"""""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
