# Pandigital Primes

from itertools import permutations
from functools import reduce
from tools.prime import is_prime

digits = list(range(1, 10))

done = False

while not done:
    nums = []
    for number_list in permutations(digits, len(digits)):
        nums.append(int(reduce(lambda x, y: str(x) + str(y), number_list)))

    list.sort(nums, reverse=True)

    for num in nums:
        if is_prime(num):
            done = True
            break

    digits.pop()
    if len(digits) == 0:
        break

if done:
    print(num)
