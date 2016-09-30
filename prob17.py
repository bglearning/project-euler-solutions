# Problem 17
# Number Letter Counts

count = len('onethousand')

lengths = {1: len('one'), 2: len('two'), 3: len('three'), 4: len('four'),
           5: len('five'), 6: len('six'), 7: len('seven'), 8: len('eight'),
           9: len('nine'), 10: len('ten'), 11: len('eleven'),
           12: len('twelve'), 13: len('thirteen'), 14: len('fourteen'),
           15: len('fifteen'), 16: len('sixteen'), 17: len('seventeen'),
           18: len('eighteen'), 19: len('nineteen'), 20: len('twenty'),
           30: len('thirty'), 40: len('forty'), 50: len('fifty'),
           60: len('sixty'), 70: len('seventy'), 80: len('eighty'),
           90: len('ninety')}

for num in range(1, 1000):
    temp_cnt = 0
    h_val = int(num / 100)
    t_val = int(num % 100)

    if h_val != 0:
        temp_cnt += lengths[h_val] + len('hundred')

    if t_val != 0:
        if h_val != 0:
            temp_cnt += len('and')
        if 10 <= t_val < 20:
            temp_cnt += lengths[t_val]
        else:
            t_mult = int(t_val / 10)
            o_val = int(t_val % 10)
            if t_mult != 0:
                temp_cnt += lengths[t_mult * 10]
            if o_val != 0:
                temp_cnt += lengths[o_val]
    count += temp_cnt

print(count)
