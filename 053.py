import sympy

c = 0
for n in range(1, 101):
    for k in range(2, n):
        if sympy.binomial(n, k) > 1000000:
            c += 1
print(c)
