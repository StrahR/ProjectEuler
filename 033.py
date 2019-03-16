from math import gcd

pn = 1
pd = 1
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                f = (10 * a + b) / (10 * c + d)
                if f >= 1:
                    continue
                if b == c and f == a / d:
                    # print(a, b, c, d)
                    pn *= (10 * a + b)
                    pd *= (10 * c + d)
g = gcd(pn, pd)
print(pn / g, pd / g)
