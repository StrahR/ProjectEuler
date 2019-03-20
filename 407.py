target = 10**7
s = 0
for n in range(1, target+1):
    print(n)
    for a in range(n):
        m = 0
        if (a*a) % n == a:
            m = a
        s += m
print(s)
