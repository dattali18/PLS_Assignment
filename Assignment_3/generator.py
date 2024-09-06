"""
This file will contain the generator function in a functional programming paradigm.
every question need to be answered using lazy evaluation and without.
"""

# 1.
# Write a generator function that generates numbers from 0 to 10_000.


# with lazy evaluation
def generate_numbers():
    for i in range(10_001):
        yield i


# without lazy evaluation
def generate_numbers():
    return [i for i in range(10_001)]


# measuring the time it takes to generate the numbers
import time

start = time.time()
for i in generate_numbers():
    pass
print(f"tool {time.time() - start} seconds to generate the numbers")

# printing the size of the generated numbers
print(f"size of the generated numbers: {len(generate_numbers())}")

# with the above function create list containing only the number from 0 to 5_000

start = time.time()

# with lazy evaluation
numbers = [i for i in generate_numbers() if i <= 5_000]

end = time.time() - start

print(f"tool {end} seconds to generate the numbers")


# 2.
# Write a generator function that generate prime numbers and each time we call the the next function it will return the next prime number.


# with lazy evaluation
def generate_prime_numbers():
    i = 2
    while True:
        if all(i % j != 0 for j in range(2, i)):
            yield i
        i += 1


# without lazy evaluation
def generate_prime_numbers_without():
    i = 2
    prime_numbers = []
    while True:
        if all(i % j != 0 for j in range(2, i)):
            prime_numbers.append(i)
        i += 1
        return prime_numbers


# test

prime_1 = generate_prime_numbers()

assert next(prime_1) == 2
assert next(prime_1) == 3
assert next(prime_1) == 5

# 3.
# Write a generator function that generates the power of x for each number from 0 to n.

# NOTE still has problem this part

# with lazy evaluation
# using cache to store the power of x for each number
from functools import lru_cache

@lru_cache
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def power_function(n):
    return lambda x: x ** n

def e_power_x(x):
    i = 0
    while True:
        yield power_function(i)(x) / factorial(i)
        i += 1

powers = [e_power_x(2)(i) for i in range(8)]

print(powers)

assert powers == [
    1.0,
    3.0,
    5.0,
    6.333333333333333,
    7.0,
    7.266666666666667,
    7.355555555555555,
    7.3809523809523805,
]


# without lazy evaluation
def e_power_x_without(x):
    return [power_function(i)(x) / factorial(i) for i in range(8)]


assert e_power_x_without(2) == [
    1.0,
    3.0,
    5.0,
    6.333333333333333,
    7.0,
    7.266666666666667,
    7.355555555555555,
    7.3809523809523805,
]
