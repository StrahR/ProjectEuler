memory = {}
mask = 1000000

def nob(n: int, k: int) -> int:
    if (n, k) in memory:
        return memory[(n, k)]
    if n <= 0 or k <= 0:
        memory[(n, k)] = 0
        return 0
    if n == 1:
        memory[(n, k)] = 1
        return 1
    if k > n:
        c = nob(n, n) % mask
        memory[(n, k)] = c
        return c
    c = int(k == n) # wtf why
    #k1 = min(n, k)
    #if k1 == 1:
        #memory[(n, k)] = 1
        #memory[(n, k1)] = 1
        #return 1
    c += nob(n, k - 1) % mask + nob(n - k, k) % mask
    #print(n, k, c)
    memory[(n, k)] = c % mask
    #memory[(n, k1)] = c
    return c % mask


print(nob(5, 5))
n = 1000
while True:
    if n % 1000 == 0:
        print(n)
    for k in range(1, n, 100):
        nob(n, k)
    if nob(n, n) == 0:
        break
    n += 1
print(n)
