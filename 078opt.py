memory = {0: 1, 1: 1}
mask = 1000000


def P(n: int) -> int:
    n = int(n)
    if n < 0:
        return 0
    if n in memory:
        return memory[n]
    s = 0
    for k in range(1, n + 1):
        s += ((-1) ** (k + 1)) * (P(n - k * (3 * k - 1) / 2) + P(n - k * (3 * k + 1) / 2))
    memory[n] = s % mask
    return s % mask


print(P(5))
n = 500
while True:
    if n % 1000 == 0:
        print(n)
    # for k in range(1, n, 100):
    #     P(n)
    if P(n) == 0:
        break
    n += 1
print(n)
