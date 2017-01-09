# Problem 36
# Double-base palindromes

palindrome_sum = 0

for num in range(1, 1000000, 2):
    binary_str = bin(num)[2:]
    num_str = str(num)

    if num_str == num_str[::-1] and binary_str == binary_str[::-1]:
        palindrome_sum += num

print(palindrome_sum)
