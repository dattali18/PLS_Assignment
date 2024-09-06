"""
This file will demonstrate the use of recursion in Python. in a functional programming style to solve problems.
"""

# Using recursion create a tuple with the numbers 1 - 1_000
# there is a problem with max recursion depth remove this limit
import sys

sys.setrecursionlimit(10_000)

def create_numbers(n: int):
    if n == 1:
        return (1,)
    return create_numbers(n - 1) + (n,)

# Tail recursion
def create_numbers_2():
    def create_numbers_tail(n: int, acc=()):
        if n == 1:
            return acc + (1,)
        return create_numbers_tail(n - 1, acc + (n,))
    return create_numbers_tail(1_000)

# test both functions
print(create_numbers(1_000))
print(create_numbers_2())
