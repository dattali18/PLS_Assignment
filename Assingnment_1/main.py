def getPentaNum(n):
    return n * (3 * n - 1) // 2


def pentaNumRange(n1, n2):
    return [getPentaNum(i) for i in range(n1, n2)]


def sumDigit(n):
    """
    This is not the best way to do it
    the simplest way to do it is $$sum(n) = n * (n+1) / 2$$
    but in this assignment we are not allowed to use it
    """
    return sum([int(i) for i in str(n)])


def get_gematria(word):
    gematria = {
        "א": 1,
        "ב": 2,
        "ג": 3,
        "ד": 4,
        "ה": 5,
        "ו": 6,
        "ז": 7,
        "ח": 8,
        "ט": 9,
        "י": 10,
        "כ": 20,
        "ל": 30,
        "מ": 40,
        "נ": 50,
        "ס": 60,
        "ע": 70,
        "פ": 80,
        "צ": 90,
        "ק": 100,
        "ר": 200,
        "ש": 300,
        "ת": 400,
    }

    # NOTE that in the hebrew language the letters are written from right to left
    # NOTE that in the gematria we have special way to write 15 and 16 they are not write as 10+5 and 10+6 but has 9 + 6 and 9 + 7
    # so the string "טו" is 15 and "טז" is 16

    # we will use the gematria dictionary to get the value of each letter in the word
    # and sum them all loop from right to left and check if the letter is in the gematria dictionary

    sum = 0
    reversed_word = word[::-1]

    for i in range(len(reversed_word)):
        if reversed_word[i] in gematria:
            # check if the letter is 15 or 16
            if i > 0 and reversed_word[i] == "ו" and reversed_word[i - 1] == "ט":
                sum += 6 + 9
                continue
            sum += gematria[reversed_word[i]]
        else:
            raise ValueError(
                f"the letter {reversed_word[i]} is not in the gematria dictionary"
            )

    return sum


def is_prime(n):
    if n < 2:
        return False
    # looping from 2 to the  √n (sqrt(n))
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def has_twin_prime(n):
    is_prime_n = is_prime(n)
    if not is_prime_n:
        return False
    if is_prime(n + 2) or is_prime(n - 2):
        return True
    return False


def get_twin_prime_up_to_n(n):
    twin_primes = {}
    for i in range(2, n):
        if has_twin_prime(i):
            twin_primes[i] = i + 2 if is_prime(i + 2) else i - 2
    return twin_primes


def add3dicts(d1, d2, d3):
    new_dict = {}
    for key in d1:
        new_dict[key] = (d1[key], d2[key], d3[key])
    return new_dict


def apply_functions_on_numbers(numbers, functions):
    functions_dict = {}
    for func in functions:
        functions_dict[func.__name__] = [func(number) for number in numbers]
    return functions_dict


def multiply_by_2(x):
    return x * 2


def square(x):
    return x**2


def inverse(x):
    return 1 / x

functions = [multiply_by_2, square, inverse]
