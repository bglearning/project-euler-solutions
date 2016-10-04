# Problem 15
# Routes through a 20 x 20 grid

# Method 1
# Just use the formula 40!/((20!)(20!))
# It is a combination of 40 zeroes and ones, with the restriction
# that there has to be 20 of each.

from math import factorial

print(factorial(40)/(factorial(20)**2))

# Method 2

n = 20
grid_points = [[0] * (n + 2) for i in range(0, n + 2)]

grid_points[1][0] = 1

for row in range(1, n+2):
    for col in range(1, n+2):
        grid_points[row][col] = (grid_points[row-1][col]
                                 + grid_points[row][col-1])

print(grid_points[n+1][n+1])
