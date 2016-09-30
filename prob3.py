# Problem 3
# The largest prime factor of the number

from prime import is_prime
from math import sqrt

num = 600851475143

for i in range(int(sqrt(num)),2,-1):
    if num%i == 0 and is_prime(i):
        print(i)
        break

    




