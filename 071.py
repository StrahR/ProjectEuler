max_n = 0
max_d = 1
lim = 1000000
for d in range(lim + 1):
    n = (3 * d) // 7 - 1
    # print(n, d)
    if n * max_d > max_n * d:
        max_n = n
        max_d = d
print(max_n, max_d, max_n / max_d)
