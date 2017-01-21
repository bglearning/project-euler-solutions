# Problem 39
# Integer Right Triangles

from math import sqrt

perimeter_map = [0] * 1000

for a in range(1, 999):
    for b in range(1, 999):
        h = sqrt(a * a + b * b)
        perimeter = int(a + b + h)
        if perimeter > 1000:
            break
        if not h.is_integer():
            continue
        perimeter_map[perimeter - 1] += 1

max_count = 0
max_perimeter = 0

for i in range(0, 1000):
    if perimeter_map[i] > max_count:
        max_perimeter = i + 1
        max_count = perimeter_map[i]

print(max_count)
print(max_perimeter)
