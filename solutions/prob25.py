# Problem 25
# Index of first Fibonacci number to have 1000 digits

from math import sqrt
from math import log

limit = 1000

# Method 1
lower = 1
higher = 1
index = 2

while True:
    if len(str(higher)) >= limit:
        break
    lower, higher = higher, lower + higher
    index += 1

print(index)

# Method 2

# The nth Fibonacci number is [phi**n / sqrt(5)], where the
# brackets denote "nearest integer".
#
# So we need phi**n/sqrt(5) > 10**999
#
# n * log(phi) - log(5)/2 > 999 * log(10)
#
# n * log(phi) > 999 * log(10) + log(5)/2
# n > (999 * log(10) + log(5) / 2) / log(phi)

phi = (1 + sqrt(5)) / 2
n = int(((limit - 1) * log(10) + log(5) / 2) / log(phi))
print(n + 1)
