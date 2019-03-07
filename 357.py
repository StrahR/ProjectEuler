"""
n+1 \in P
proper divisors only

"""
from math import floor, sqrt
from strah import sieve, is_composite

'''
def sieve(end):
    sieve_list = list(range(end))
    sieve_list[1] = 0
    for i in range(2, floor(sqrt(end) + 1)):
        if sieve_list[i]:
            for mult in range(2 * i, end, i):
                sieve_list[mult] = 0
    return [p for p in sieve_list if p != 0]


def divisor_list(n: int) -> set:
    r = set()
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            r.add(i)
            #r.append(int(n / i)) # only the lower one is needed 
    return(r)
'''

target = 100000000
prime_list = sorted(sieve(target))

prime_list2 = sieve(100)
composite_list2 = list(set(range(1, 100)) - set(prime_list2))
'''
def is_composite(n: int) -> bool:
    if n == 2 or n == 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    for i in range(5, floor(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return True
    return False
'''

def is_prime_generating(n: int) -> bool:
    for d in range(2, floor(sqrt(n)) + 1):
        if n % d == 0 and is_composite(d + n // d):
            return False
    return True

import time
print(time.ctime())
s = 0
for p in prime_list:
    #print(p)
    if is_prime_generating(p-1):
        s += p - 1
print(s)
print(time.ctime())
