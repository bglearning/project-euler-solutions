# Problem 21
# Amicable Numbers

from math import sqrt


def d(num):
    div_sum = 1
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            div_sum += i + num / i
            if sqrt(num) % i == 0:
                div_sum -= i
    return div_sum

amicable_sum = 0

checkbox = [0] * 10000
checkbox[0] = 0

for n in range(2, 10000):
    if checkbox[int(n - 1)] == 1:
        continue
    d_n = d(n)
    if d(d_n) == n and d_n != n:
        amicable_sum += n + d_n
        checkbox[int(n - 1)] = 1
        checkbox[int(d_n - 1)] = 1

print(amicable_sum)
