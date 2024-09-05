# **************************** Part 2 ***************************
# 2.1
lst = list(range(0, 1_000))

is_even = lambda x: x % 2 == 0
is_odd = lambda x: x % 2 != 0 # or lambda x: not is_even(x)

# divide the list into two lists, one for even numbers and the other for odd numbers
even_numbers = list(filter(is_even, lst))
odd_numbers = list(filter(is_odd, lst))

# 2.2
multiply_successive = lambda x, y: x * y

multiplied_even = [multiply_successive(even_numbers[i], even_numbers[i + 1]) for i in range(0, len(even_numbers) - 1, 2)]
print(multiplied_even)

linear_eq = lambda x, next: x / 2 + 2 + next

# applied the linear_eq function to the odd numbers
applied_odd = [linear_eq(odd_numbers[i], odd_numbers[i + 1]) for i in range(0, len(odd_numbers) - 1, 2)]

# 2.3

# sum both lists by themselves
print(sum(multiplied_even))
print(sum(applied_odd))

