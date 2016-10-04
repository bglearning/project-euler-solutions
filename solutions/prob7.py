# Problem 7
# 10001st Prime

from tools.prime import is_prime

count = 2  # For the numbers 2 and 3
candidate = 3

while count < 10001:
    candidate += 2
    if is_prime(candidate):
        count += 1

print(candidate)
