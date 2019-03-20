import time


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def n(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    if (a, b) not in mem:
        mem[(a, b)] = ((a+1)*(b+1) - (1+gcd(a, b))) // 2
    return mem[(a, b)]


def N(a: int, b: int, c: int, d: int) -> int:
    return (n(a, b)
            + n(b, c)
            + n(c, d)
            + n(a, d)
            - (a+b+c+d)  # overcounted along `x` and `y` axes
            + 1)  # undercounted `(0, 0)`


def is_square(n: int) -> bool:
    return int(n**(1/2))**2 == n


m = 40
tot = 0
mem = {}
for a in range(1, m+1):
    for b in range(a, m+1):
        for c in range(b, m+1):
            for d in range(c, m+1):
                sq = N(a, b, c, d)
                if a == b == c == d:
                    tot += 1 if is_square(sq) else 0
                elif a == b == c or b == c == d:
                    tot += 4 if is_square(sq) else 0
                elif a == b and c == d:
                    tot += 4 if is_square(sq) else 0
                    sq = N(a, c, b, d)
                    tot += 2 if is_square(sq) else 0
                elif a == b or b == c or c == d:
                    tot += 8 if is_square(sq) else 0
                    if b == c:
                        sq = N(a, b, d, c)
                        tot += 4 if is_square(sq) else 0
                    else:
                        sq = N(a, c, b, d)
                        tot += 4 if is_square(sq) else 0
                else:
                    tot += 8 if is_square(sq) else 0
                    sq = N(a, c, b, d)
                    tot += 8 if is_square(sq) else 0
                    sq = N(a, b, d, c)
                    tot += 8 if is_square(sq) else 0
print(tot, time.process_time())
