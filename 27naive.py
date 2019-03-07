from strah import is_prime

mn = 0
pr = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while is_prime(n * (n + a) + b):
            n += 1
        n -= 1
        if n > mn:
            print(a, b)
            mn = n
            pr = a * b
print(pr)
