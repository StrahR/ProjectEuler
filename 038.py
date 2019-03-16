from strah import is_pandigital


def concatenated_product(k: int, n: int) -> int:
    s = ''
    for i in range(1, n + 1):
        s += str(k * i)  # concat
    return int(s)


maxp = 0
for n in range(2, 10):
    for k in range(1, 100000):
        p = concatenated_product(k, n)
        if is_pandigital(p):
            maxp = max(p, maxp)
print(maxp)
