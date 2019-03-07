memory = {}

def sieve(end):
    prime_list = []
    sieve_list = list(range(end))
    for i in range(2, end):
        if sieve_list[i]:
            prime_list.append(i)
            for mult in range(2 * i, end, i):
                sieve_list[mult] = 0
    return prime_list



def nob(n: int, primes) -> int:
    if n == 0 or len(primes) == 0:
        return 0
    i = 0
    while i < len(primes) and primes[i] < n:
        i += 1
    c = int(i < len(primes) and primes[i] == n)
    if i > 0:
        c += nob(n, primes[:i - 1]) + nob(n - primes[i - 1], primes[:i])
    #print(n, primes, c)
    return c


target = 100

prime_list = sorted(sieve(target))

for n in range(10, target):
    if nob(n, prime_list) > 5000:
        print(n)
        break
