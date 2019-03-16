from strah import sieve
import time

m = 0
mnphin = 10
# for n in sorted(range(10**6 + 1, 10**7, 2), reverse=True):
#     # if (n-1) % 100000 == 0:
#         # print(n-1, m, mnphin)
#     # phin = phi(n)
#     # exclude low prime factors
#     if n % 3 == 0:
#         continue
#     if n % 5 == 0:
#         continue
#     if n % 7 == 0:
#         continue
#     if n % 11 == 0:
#         continue
#     if n % 13 == 0:
#         continue
#     if n % 17 == 0:
#         continue
#     if n % 23 == 0:
#         continue
#     if n % 27 == 0:
#         continue
#     if n % 29 == 0:
#         continue
#     if n % 31 == 0:
#         continue
#     if n % 37 == 0:
#         continue
#     if n % 41 == 0:
#         continue
#     if n % 43 == 0:
#         continue
#     if n % 47 == 0:
#         continue
#     if n % 53 == 0:
#         continue
#     if n % 59 == 0:
#         continue
#     if n % 61 == 0:
#         continue
#     if n % 67 == 0:
#         continue
#     if n % 71 == 0:
#         continue
#     if n % 73 == 0:
#         continue
#     if n % 79 == 0:
#         continue
#     if n % 83 == 0:
#         continue
#     if n % 89 == 0:
#         continue
#     if n % 97 == 0:
#         continue
#     factors = prime_factors(n)
#     r = n
#     for p in factors:
#         r *= 1 - 1 / p
#     phin = round(r)

primes = sieve(10**5)[0]
for i in range(primes.index(3163), len(primes)):
    for j in range(primes.index(1009), i):
        n = primes[i] * primes[j]
        if n > 10**7:
            break
        phin = (primes[i] - 1) * (primes[j] - 1)
        if sorted(str(n)) == sorted(str(phin)) and n / phin < mnphin:
            mnphin = n / phin
            m = n
            print(n)
print(m)
print(time.process_time())
