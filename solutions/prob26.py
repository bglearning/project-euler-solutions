# Problem 26
# Reciprocal Cycles

d = 0
ans = 0

for num in range(2, 1000):
    numerator = 1
    o_list = []
    d_temp = 0
    while True:
        ten_fold_cnt = 0
        while numerator < num:
            numerator *= 10
            ten_fold_cnt += 1
            if ten_fold_cnt > 1:
                o_list.append(0)
        rem = numerator % num
        # Perfectly divisible
        if rem == 0:
            break
        numerator = rem
        # If Cycle found
        if rem in o_list:
            d_temp = len(o_list) - o_list.index(rem)
            break
        o_list.append(rem)
    if d_temp > d:
        d = d_temp
        ans = num

print(str(ans) + ':' + str(d))
