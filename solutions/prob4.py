# Problem 4
# Largest palindrome made from the product of two 3-digit numbers

from tools.number_tools import is_palindrome
from time import perf_counter

start = perf_counter()
greatest = 999 * 999
done = False

'''
biggest = 0
for i in range(100, 1000):
    for j in range(110, 1000, 11):
        candidate = i * j
        if is_palindrome(candidate) and candidate > biggest:
            biggest = candidate

print(biggest)
'''


for num in range(greatest, 10000, -1):
    if done:
        break
    if is_palindrome(num):
        for div in range(100, 999):
            if num % div == 0 and len(str(int(num / div))) == 3:
                done = True
                break
print(num + 1)
print('Total time = ', perf_counter() - start)
