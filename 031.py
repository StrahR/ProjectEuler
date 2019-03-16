# denominations = [200, 100, 50, 20, 10, 5, 2, 1]
# rdenominations = reversed(denominations)


def nob(n: int, denominations) -> int:
    if n == 0 or len(denominations) == 0:
        return 0
    i = 0
    while i < len(denominations) and denominations[i] < n:
        i += 1
    c = int(i < len(denominations) and denominations[i] == n)
    if i > 0:
        c += (nob(n, denominations[: i-1])
              + nob(n - denominations[i-1], denominations[: i]))
    # print(n, denominations, c)
    return c


print(nob(200, [1, 2, 5, 10, 20, 50, 100, 200]))
# print([1,2,3,4][: -1])
