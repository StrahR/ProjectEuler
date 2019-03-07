from datetime import datetime

c = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime(year, month, 1).strftime("%w") == '0':
            c += 1
print(c)
