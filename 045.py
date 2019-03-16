def T(n: int) -> int:
    return n * (n+1) // 2


def P(n: int) -> int:
    return n * (3*n - 1) // 2


def H(n: int) -> int:
    return n * (2*n - 1)


tn = 286
pn = 166
hn = 144
while True:
    while T(tn) < P(pn) or T(tn) < H(hn):
        tn += 1
    while P(pn) < H(hn):
        pn += 1
    while H(hn) < P(hn):
        hn += 1

    if T(tn) == H(hn) and T(tn) == P(pn):
        break

    tn += 1
    pn += 1
    hn += 1

print(T(tn))
