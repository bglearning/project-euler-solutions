# Problem 5
# Smallest positive number that is evenly divisible by all of the numbers
# from 1 to 20

start_num = 1000000
test_nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
done = False
while not done:
    done = True
    start_num += 20
    for i in test_nums:
        if start_num % i != 0:
            done = False
            break

print(start_num)
