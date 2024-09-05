# *************************** Part 1 ****************************

# 1.1
linear_eq = lambda x: x / 2 + 1

# 1.2
new_arr = [linear_eq(x) for x in range(0, 10_000)]
# another way is to do it like to
numbers = range(0, 10_000)
# new_arr = list(map(linear_eq, numbers))

# 1.3
def sum_list_with_function(numbers, function):
    # or
    # return sum(map(function, numbers))
    return sum([function(x) for x in numbers])

# 1.4
# comparing the time of the two methods
import time

start = time.time()
sum_1 = sum_list_with_function(numbers, linear_eq)
end = time.time()
print("Time for list comprehension: ", end - start)

start = time.time()
sum_2 = sum([x / 2 + 2 for x in numbers])
end = time.time()
print("Time for list comprehension: ", end - start)

