import time
from math import floor, sqrt
from strah import sieve, is_composite

target = 100000000
prime_list = sorted(sieve(target)[0])

prime_list2 = sieve(100)
composite_list2 = list(set(range(1, 100)) - set(prime_list2))


def is_prime_generating(n: int) -> bool:
    for d in range(2, floor(sqrt(n)) + 1):
        if n % d == 0 and is_composite(d + n // d):
            return False
    return True


print(time.ctime())
s = 0
for p in prime_list:
    # print(p)
    if is_prime_generating(p-1):
        s += p - 1
print(s)
print(time.ctime())
