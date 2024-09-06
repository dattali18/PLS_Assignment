"""
This file will demonstrate the use of recursion in Python. in a functional programming style to solve problems.
"""

# 1

# Using recursion create a tuple with the numbers 1 - 1_000
# there is a problem with max recursion depth remove this limit
import sys

sys.setrecursionlimit(10_000)


def create_numbers(n: int) -> tuple:
    if n == 1:
        return (1,)
    return create_numbers(n - 1) + (n,)


# Tail recursion
def create_numbers_tail() -> tuple:
    def inner(n: int, acc=()) -> tuple:
        if n == 1:
            return (1,) + acc
        return inner(n - 1, (n,) + acc)

    return inner(1_000)


# test both functions
numbers_tuple_1 = create_numbers(1_000)
numbers_tuple_2 = create_numbers_tail()


assert numbers_tuple_1 == numbers_tuple_2
assert numbers_tuple_1 == tuple(range(1, 1_001))


# 2
# sum the numbers in the tuple using recursion again using both normal and tail recursion
def sum_numbers(numbers: tuple) -> int:
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + sum_numbers(numbers[1:])


# Tail recursion
def sum_numbers_tail(numbers: tuple) -> int:
    def inner(numbers: tuple, acc: int = 0) -> int:
        if len(numbers) == 1:
            return acc + numbers[0]
        return inner(numbers[1:], acc + numbers[0])

    return inner(numbers)


sum_1 = sum_numbers(numbers_tuple_1)
sum_2 = sum_numbers_tail(numbers_tuple_1)

assert sum_1 == sum_2
assert sum_1 == 500_500

# 3
# write the LCM (Least Common Multiplier) algorithm using recursion


def lcm(a: int, b: int) -> int:
    if b == 0:
        return a
    return lcm(b, a % b)


def tail_lcm(a: int, b: int) -> int:
    def inner(a: int, b: int) -> int:
        if b == 0:
            return a
        return inner(b, a % b)

    return inner(a, b)


# test the functions

lcm_1 = lcm(10, 5)
lcm_2 = tail_lcm(10, 5)

assert lcm_1 == 5
assert lcm_2 == 5

# 4.
#  write a recursive function the check if a number is a palindrome

def recursive_is_palindrome(n: int) -> bool:
    n = str(n)
    if len(n) <= 1:
        return True
    if n[0] != n[-1]:
        return False
    return recursive_is_palindrome(n[1:-1])

def recursive_is_palindrome_tail(n: int) -> bool:
    def inner(n: str) -> bool:
        if len(n) <= 1:
            return True
        if n[0] != n[-1]:
            return False
        return inner(n[1:-1])
    return inner(str(n))

assert recursive_is_palindrome(121) == True
assert recursive_is_palindrome(122) == False

# 5.
# write a recursive function "sortedzip" that receive a list of lists using the sorted function and return their sorted zip
# example input: list(sortedzip([[3,1,2],[5,6,4],['a','b','c']])) -> [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]

def sortedzip(lists: list) -> list:
    lists = [sorted(l) for l in lists]
    if not all(lists):
        return []
    return [tuple(l.pop(0) for l in lists)] + sortedzip(lists)

assert list(sortedzip([[3,1,2],[5,6,4],['a','b','c']])) == [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]