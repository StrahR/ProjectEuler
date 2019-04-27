import math


def sigma(n: int) -> int:
    r = [0] * (n+1)
    while n % 2 == 0:
        r[2] += 1
        n //= 2

    while n % 3 == 0:
        r[3] += 1
        n //= 3

    for i in range(5, math.floor(math.sqrt(n)) + 1, 6):
        while n % i == 0:
            r[i] += 1
            n //= i

        while n % (i + 2) == 0:
            r[i+2] += 1
            n //= (i + 2)

    if n > 2:  # if n is prime
        r[n] += 1

    # p = [i for i in range(n) if r[i] > 0]
    # a = [r[i] for i in range(n) if r[i] > 0]
    # print(r, p, a)
    prod = 1
    for i in range(2, len(r)):
        prod *= (i**(r[i]+1) - 1) / (i - 1)
    return int(prod)


print(sigma(2500))


D = [0] * 


