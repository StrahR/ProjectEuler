from math import sqrt, floor


def is_pandigital(a: int, b: int, n: int) -> bool:
    return (len(str(a) + str(b) + str(n)) == 9
            and len(set(list(str(a) + str(b) + str(n) + '0'))) == 10)


# print(is_pandigital(123, 536, 789))
s = 0
for i in range(4000, 8000):
    for d in range(2, floor(sqrt(i)) + 1):
        if i % d == 0 and is_pandigital(d, i // d, i):
            # print(i, d, i // d)
            s += i
            break
print(s)
