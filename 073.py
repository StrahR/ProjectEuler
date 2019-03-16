from math import gcd
lim = 12000
c = 0
for d in range(5, lim + 1):
    for n in range(d // 3 + 1, (d + 1) // 2):
        # print(n, d)
        if gcd(n, d) == 1:
            c += 1
print(c)
