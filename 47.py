from strah import omega

n = 10
i = 0
k = 4
while True:
    if omega(n) == k:
        i += 1
    else:
        i = 0
    if i == k:
        print(n - k + 1)
        break
    n += 1
