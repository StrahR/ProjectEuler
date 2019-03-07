memory = {}

def nob(n: int, k: int) -> int:
    if (n, k) in memory:
        return memory[(n, k)]
    if n <= 0 or k <= 0:
        memory[(n, k)] = 0
        return 0
    c = int(k >= n) # wtf why
    k1 = min(n, k)
    if k1 == 1:
        memory[(n, k)] = c
        memory[(n, k1)] = 1
        return 1
    c += nob(n, k1 - 1) + nob(n - k1, k1)
    #print(n, k, c)
    memory[(n, k)] = c
    memory[(n, k1)] = c
    return c


print(nob(100, 99))
