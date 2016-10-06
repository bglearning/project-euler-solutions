# Problem 30
# Digit fifth powers

num_sum = 0
# We only need to check numbers with 6 or less digits
# as (9**5) * 7 is a six digit number (413343)
for num in range(10, 1000000):
    if num == sum(int(ch)**5 for ch in str(num)):
        num_sum += num
print(num_sum)
