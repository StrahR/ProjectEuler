n = 1
m = 1
i = 1
while len(str(n)) < 1000:
    # print(i, n)
    temp = m + n
    n = m
    m = temp
    i += 1

print(i)  # 4782
