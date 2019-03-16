from math import floor, sqrt

mask = 500500507

p = 1
for i in range(2, 2 ** 3):
    p *= i
print(p)


def nod(n: int) -> list:
    r = [1]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            r.append(i)
    r.append(n)
    return r


def nop(n: int) -> list:
    r = list()
    while n % 2 == 0:
        r.append(2)
        n /= 2

    while n % 3 == 0:
        r.append(3)
        n /= 3

    for i in range(5, floor(sqrt(n)) + 1, 6):
        while n % i == 0:
            r.append(i)
            n /= i

        while n % (i + 2) == 0:
            r.append(i + 2)
            n /= (i + 2)

    if n > 2:
        r.append(n)

    return r
