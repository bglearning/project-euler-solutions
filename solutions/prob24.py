# Problem 24
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from math import factorial

target = 999999
choice_cnt = 10
choices = [i for i in range(choice_cnt)]
ans = ''

while choice_cnt > 0:
    total_possible = factorial(choice_cnt)
    choice_space = int(total_possible / choice_cnt)
    i = int(target / choice_space)
    ans += str(choices.pop(i))
    target = target % choice_space
    choice_cnt -= 1

print(ans)
