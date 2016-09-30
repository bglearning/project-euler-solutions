# Problem 2
# By considering the terms in the Fibonacci sequence 
# whose values do not exceed four million, find the 
# sum of the even-valued terms.

first,second = 1,2
sum = 0

while second<4000000:
    if second%2==0:
        sum += second

    temp = first
    first = second
    second = temp + second

print(sum)

