# Problem 27
# Quadratic Primes

from tools.prime import is_prime

longest = 0
ans = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        temp_cnt = 0
        while is_prime(n * n + a * n + b):
            temp_cnt += 1
            n += 1
        if temp_cnt > longest:
            ans = a * b
            longest = temp_cnt

print(ans)
