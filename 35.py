from strah import sieve, is_prime

target = 1000000
primes = sieve(target)

c = len(primes)
for p in primes:
    d = len(str(p))
    for i in range(1, d):
        n = int(str(p)[-i:] + str(p)[:-i])
        if not is_prime(n):
            c -= 1
            break
print(c)
