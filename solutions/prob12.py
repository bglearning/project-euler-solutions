# Problem 12
# Value of the first triangle number to have over five hundred divisors

from math import sqrt
from time import perf_counter


def num_of_divisors(num):
    div_count = 2
    for div in range(2, int(sqrt(num))):
        if num % div == 0:
            div_count += 2
    if (sqrt(num) - int(sqrt(num))) == 0:
        div_count -= 1
    return div_count

# Method 1: Brute Force
start = perf_counter()
tri_num = 1
i = 2

while True:
    tri_num += i
    i += 1

    if num_of_divisors(tri_num) > 500:
        break

print(tri_num)
print(perf_counter() - start)

# Method 2: n and (n+1) have no factors in common except 1

start2 = perf_counter()
n = 2
while True:
    div_count2 = 0
    if n % 2 == 0:
        div_count2 = num_of_divisors(int(n/2)) * num_of_divisors(n+1)
    else:
        div_count2 = num_of_divisors(n) * num_of_divisors(int(n+1)/2)

    if div_count2 > 500:
        break
    n += 1

print(n*(n+1)/2)
print(perf_counter() - start2)
