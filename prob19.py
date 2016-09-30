# Problem 19
# Sundays in the first of the month (20th Century)

import datetime

cnt = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        if datetime.datetime(y, m, 1).weekday() == 6:
            cnt += 1
print(cnt)

# Method 2

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_days(month, year):
    if month == 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return month_days[month] + 1
    return month_days[month]

start = 366
count = 0
for year in range(1901, 2001):
    for month in range(0, 12):
        if start % 7 == 0:
            count += 1
        start += get_days(month, year)

print(count)

# Method 3 | Simple Division

print(int(12*100/7))
