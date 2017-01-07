# Problem 33
# Digit Cancelling Fractions

from fractions import gcd

num_product = 1
den_product = 1

for num in range(11, 100):
    if num % 10 == 0:
        continue
    for den in range(num + 1, 100):
        if den % 10 == 0:
            continue
        common_chars = [ch for ch in str(num) if ch in str(den)]
        if not common_chars:
            continue
        replaced_num = int(str(num).replace(common_chars[0], '', 1))
        replaced_den = int(str(den).replace(common_chars[0], '', 1))
        if num * replaced_den == den * replaced_num:
            print('{} / {}'.format(num, den))
            num_product *= num
            den_product *= den

print(den_product // gcd(num_product, den_product))
