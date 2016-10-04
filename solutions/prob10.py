# Problem 10
# Summation of primes

from tools.prime import is_prime
from time import perf_counter

limit = 2000000

# Method 1
start1 = perf_counter()
sum = 2  # Initialized by adding two
num = 3

while num < limit:
    if is_prime(num):
        sum += num
    num += 2

print(sum)
print('Time: ', perf_counter() - start1)

# Method 2 : Prime Sieve
start2 = perf_counter()
marked = [0] * limit
value = 3
s = 2
while value < limit:
    if marked[value] == 0:
        s += value
        i = value
        while i < limit:
            marked[i] = 1
            i += value
    value += 2
print(s)
print('Time: ', perf_counter() - start2)
