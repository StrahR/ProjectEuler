def mul_mod(a: int, b: int, m: int) -> int:
    d = 0
    a %= m
    b %= m

    for i in range(64):
        d *= 2
        d %= m

        if a & 0x8000000000000000:
            d += b
        d %= m
        a *= 2

    return d


def pow_mod(a: int, b: int, m: int) -> int:
    r = m == 1 and 0 or 1
    while b > 0:
        if b & 1:
            r = mul_mod(r, a, m)
        b = b // 2
        a = mul_mod(a, a, m)
    return r


# print(pow_mod(2, 4, 5))
a = 1777
for i in range(1855):
    # a = pow_mod(1777, a, 100000000)
    a = pow(1777, a, 100000000)
print(a)
