# Problem 31
# Coin Sums

# Key Idea;
# We can divide all set solutions in two sets.
# 1) Solutions that do not contain mth coin (or Sm).
# 2) Solutions that contain at least one Sm.

target_num = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]


# Method 1: Recursive Solution
def count_combos(coins, m, n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0 and n >= 1:
        return 0
    return count_combos(coins, m - 1, n) +\
        count_combos(coins, m, n - coins[m - 1])


print(count_combos(coins, len(coins), target_num))

# Method 2: Dynamic Programming

arr = [[0 for x in range(len(coins))] for y in range(target_num + 1)]
for m in range(0, len(coins)):
    arr[0][m] = 1

for num in range(1, target_num + 1):
    for m in range(0, len(coins)):
        arr[num][m] = arr[num][m - 1] + arr[num - coins[m - 1]][m]

print(arr[num][len(coins) - 1])
