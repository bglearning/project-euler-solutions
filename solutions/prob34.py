# Problem 34
# Digit factorials

# Key idea:
# We break when it's no longer possible for the sum
# of factorials of digit can reach the number even
# when all digits are 9s.

from math import factorial

num = 10
number_sum = 0

factorials = [factorial(digit) for digit in range(0, 10)]

max_num_len = 1
while max_num_len <= len(str(factorial(9) * max_num_len)):
    max_num_len += 1

while True:
    num_len = len(str(num))
    if num_len >= max_num_len:
        break
    if num == sum(factorials[int(digit)] for digit in str(num)):
        number_sum += num
    num += 1

print(number_sum)
