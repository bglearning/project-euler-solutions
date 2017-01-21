# Problem 38
# Pandigital Multiples

# Key Idea:
# The number to be multiplied must begin with 9
# Could be 9_, 9__, 9___
# Note: It looks like it can only be 9___. Oh well.

from math import pow

def is_pandigital(num):
    digit_map = [False] * 9
    if len(num) != 9:
        return False
    pandigital = True
    for digit in num:
        if digit == '0' or digit_map[int(digit) - 1 ]:
            pandigital = False
            break
        digit_map[int(digit) - 1] = True
    
    return pandigital


running_num = ''
pandigital_candidate = 0

for pow_of_ten in range(0, 4):
    start_num = int(9 * pow(10, pow_of_ten))
    limit = int(pow(10, pow_of_ten + 1))

    while start_num < limit:
        num = 2
        running_num = str(start_num)
        while True:
            running_num += str(start_num * num)
            num += 1
            if len(str(running_num)) >= 9:
                break

        if is_pandigital(running_num):
            if (int(running_num)) > pandigital_candidate:
                pandigital_candidate = int(running_num)
        start_num += 1

print(pandigital_candidate)
