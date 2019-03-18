target = 10**7
s = 0
for n in range(1, target+1):
    for a in reversed(range(n)):
        if (a*a) % n == a:
            s += a
            break
print(s)
