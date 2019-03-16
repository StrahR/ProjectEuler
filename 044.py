import math

def is_pentagonal(n: int) -> bool:
    return (1 + math.sqrt(1 + 24*n)) % 6 == 0

def P(n: int) -> int:
    return (3*n - 1)*n // 2

# print(is_pentagonal(1))
# print(is_pentagonal(5))
# print(is_pentagonal(12))
# print(is_pentagonal(70))
# print(is_pentagonal(11))
# print(is_pentagonal(P(7)))

minD = 10**8
i = 0
while True:
    i += 1
    if i > (minD-1) / 3: # P(i+1) - P(i) = 3i + 1 and if P(i+1) - P(i) > minD we can end.
        break
    Pi = P(i)
    Pip1 = P(i+1)

    d = i
    while d > 1:
        d -= 1
        Pd = P(d)
        if Pi - Pd > minD:
            break
        if Pd + Pi < Pip1:
            break
        if is_pentagonal(Pi + Pd) and is_pentagonal(Pi - Pd):
            minD = min(minD, Pi - Pd)
            print(i, d, minD)
    print(i, minD)
print(minD)