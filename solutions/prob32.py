# Problem 32
# Pandigital products

# Key idea:
# Only
# 1-digit x 4-digit = 4-digit and
# 2-digit x 3-digit = 4-digit combos are possible.

from itertools import permutations
from functools import reduce


def evaluate_product(numbers, num1_length, num2_length):
    digit_map = [False] * 9
    for n in numbers:
        digit_map[n - 1] = True
    num_a = (int(reduce(lambda x, y: str(x) + str(y),
                 numbers[0: num1_length])))
    num_b = (int(reduce(lambda x, y: str(x) + str(y),
                 numbers[num1_length: num1_length + num2_length])))
    product = num_a * num_b
    pandigital = True
    for digit in str(product):
        if digit == '0' or digit_map[int(digit) - 1]:
            pandigital = False
            break
        digit_map[int(digit) - 1] = True

    if pandigital:
        print('{} x {} = {}'.format(num_a, num_b, product))
        return product
    return 0


digits = list(range(1, 10))

products = set()

for numbers in permutations(digits, 5):
    # _ x ____ = ____ form
    products.add(evaluate_product(numbers, 1, 4))

    # __ x ___ = ____ form
    products.add(evaluate_product(numbers, 2, 3))

print(sum(products))
