# Problem 35
# Circular primes

# Key Ideas:
# For numbers with more than one digit,
# it must only be made up of digits 1, 3, 7, 9.

from tools.prime import is_prime

allowed_digits = '1379'
limit = 1000000
cnt = 4  # Single digit numbers already counted

for num in range(11, limit + 1, 2):
    num_str = str(num)
    if any(ch not in allowed_digits for ch in num_str):
        continue
    is_circular_prime = True
    for first_digit_index in range(0, len(num_str)):
        circular_num = int(num_str[first_digit_index:]
                           + num_str[:first_digit_index])
        if not is_prime(circular_num):
            is_circular_prime = False
            break

    if is_circular_prime:
        cnt += 1

print(cnt)
