# Problem 25
# Index of first Fibonacci number to have 1000 digits

lower = 1
higher = 1
index = 2
limit = 1000

while True:
    if len(str(higher)) >= limit:
        break
    lower, higher = higher, lower + higher
    index += 1

print(index)
