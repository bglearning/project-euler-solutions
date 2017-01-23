# Problem 40
# Champernowne's constant

# Key idea: We can know when the number of digts in
# a number changes.

from functools import reduce


def d(target_index):
    str_len = 0
    num_len = 1
    actual_num = 0

    while True:
        loop_num_cnt = 9 * 10**(num_len - 1)
        str_len += num_len * loop_num_cnt
        actual_num += loop_num_cnt
        if target_index <= str_len:
            break
        num_len += 1

    diff = str_len - target_index
    actual_num -= int(diff / num_len)
    character_index = num_len - (diff % num_len)
    return str(actual_num)[character_index - 1]

print(reduce(lambda x, y: x * y, (int(d(10**e)) for e in range(0, 6))))
