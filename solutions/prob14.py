# Problem 14
# Longest Collatz Sequence

num_map = [0]*500000
longest = 1
answer = 0

for num in range(500000, 1000000):
    temp_lenth = 0
    temp_num = num
    if num_map[num - 500000] == 1:
        continue
    if num % 2 == 0 and (num - 1) % 3 == 0:
        num_map[num-500000] = 1
        continue

    while temp_num != 1:
        temp_lenth += 1
        if temp_num % 2 == 0:
            temp_num /= 2
        else:
            temp_num = 3 * temp_num + 1

        if 500000 <= temp_num < 1000000:
            num_map[int(temp_num) - 500000] = 1

    if temp_lenth > longest:
        longest = temp_lenth
        answer = num

print(answer)
