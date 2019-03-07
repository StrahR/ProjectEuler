from strah import sieve, is_pandigital

primes = sieve(10 ** 8)


m = 1234
for p in primes:
    if is_pandigital(p, len(str(p))):
        m = max(m, p)
print(m)
