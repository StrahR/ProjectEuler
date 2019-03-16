from strah import is_prime


def is_right_truncatable(n: int) -> bool:
    if len(str(n)) == 1:
        return n in (2, 3, 5, 7)
    return is_prime(n) and is_right_truncatable(int(str(n)[:-1]))


def is_left_truncatable(n: int) -> bool:
    if len(str(n)) == 1:
        return n in (2, 3, 5, 7)
    return is_prime(n) and is_left_truncatable(int(str(n)[1:]))


def is_truncatable(n: int) -> bool:
    return is_left_truncatable(n) and is_right_truncatable(n)


print(is_truncatable(3797))

n = 10
c = 0
s = 0

while c < 11:
    if is_truncatable(n):
        print(n)
        c += 1
        s += n
    n += 1
print(s)
