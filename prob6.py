# Problem 6
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.

n = 100
sum_of_squares = n*(n+1)*(2*n+1)/6
square_of_sums = (n*(n+1)/2)**2

print(abs(int(sum_of_squares-square_of_sums)))
