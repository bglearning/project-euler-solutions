# Problem 23
# Non-Abundant sums

import itertools
from tools.number_tools import divisors
from time import perf_counter

# Method 1
start = perf_counter()

limit = 28124

abundant = []
for i in range(12, limit + 1):
    if sum(divisors(i)) > i:
        abundant.append(i)

possible = [0] * limit

for couple in itertools.combinations_with_replacement(abundant, 2):
    couple_sum = couple[0] + couple[1]
    if couple_sum < limit:
        possible[couple_sum] = 1

non_abundant_sum = 0
for i in range(1, limit):
    if possible[i] == 0:
        non_abundant_sum += i

print(non_abundant_sum)

print(perf_counter() - start)

# Method 2
start2 = perf_counter()

limit = 28124

divs = [[1] for i in range(limit + 1)]

for i in range(2, int(limit / 2) + 1):
    for j in range(2 * i, limit + 1, i):
        divs[j].append(i)

abuns = [abun for abun, l in enumerate(divs) if abun > 0 and sum(l) > abun]

set_sum = {m + n for m, n in itertools.combinations_with_replacement(abuns, 2)
           if m + n < limit}

n = limit - 1
total_sum = n * (n + 1) / 2

print(total_sum - sum(set_sum))

print(perf_counter() - start2)
