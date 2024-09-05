# **************************** Part 4 ***************************
# 4.1

def power_function(n):
    return lambda x: x ** n

power_2 = power_function(2)

print(power_2(2)) # 4
print(power_2(3)) # 9

# 4.2
def power_up_to(n):
    return [power_function(i) for i in range(1, n + 1)]

power_up_to_3 = power_up_to(3) # [power_function(1), power_function(2), power_function(3)]

print(power_up_to_3[0](2)) # 2^1 = 2

# 4.3
# tailor series for e^x

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def e_power_x(x, n):
    return sum([power_function(i)(x) / factorial(i) for i in range(n)])
