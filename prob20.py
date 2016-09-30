# Problem 20
# Sum of factorial digits

from functools import reduce

print(sum([int(digit) for digit in str(reduce(
    lambda x, y: x * y, range(1, 100)))]))
