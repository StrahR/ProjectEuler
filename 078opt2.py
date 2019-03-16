P = [1]
mask = 1000000

n = 1
while True:
    # if n % 1000 == 0:
    #     print(n)
    i = 0
    k = 1
    P.append(0)

    while k <= n:
        # print(n, i, k, P[n])
        s = -1 if (i % 4 > 1) else 1
        P[n] += s * P[n - k]
        P[n] %= mask
        i += 1

        j = (i // 2 + 1) if (i % 2 == 0) else -(i // 2 + 1)
        k = j * (3 * j - 1) // 2

    # print(n, P[n])
    if P[n] == 0:
        break
    n += 1
print(n)
