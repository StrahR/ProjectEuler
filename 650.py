import scipy.special
from operator import mul
from functools import reduce
from math import factorial as fac

m = 10**9 + 7
print(m)
mem = {1: 1}

def sigma(n: int) -> int:
    r = [0] * n
    while n % 2 == 0:
        r[2] += 1
        n //= 2
    
    while n % 3 == 0:
        r[3] += 1
        n //= 3
    
    for i in range(5, floor(sqrt(n)) + 1, 6):
        while n % i == 0:
            r[i] += 1
            n //= i
        
        while n % (i + 2) == 0:
            r[i+2] += 1
            n //= (i + 2)
    
    if n > 2: # if n is prime
        r[n] += 1
    
    p = [ i for i in range(n) if i ]
    a = [ r[i] for i in range(n) if i ]
    prod = 1
    for i in range(1, len(pa)):
        prod *= (p[i]**(a[i]+1) - 1) / (p[i] - 1)
    return int(prod)

def B(n: int) -> int:
    # p = 1
    # for k in range(1, n):
    #     # p *= scipy.special.comb(n, k, exact=True) % m
    #     p *= fac(n) // fac(k) // fac(n-k)
    #     p %= m
    #     # while p > m:
    #     #     p -= m
    # # return reduce(mul, [ (scipy.special.comb(n, k, exact=True) % m) for k in range(1, n) ]) % m
    # return p
    if n in mem:
        return mem[n]
    Bn = B(n-1) * n**n // fac(n)
    mem[n] = Bn
    return Bn

def D(n: int) -> int:
    # return sigma(B(n))
    return sigma(B(n)) % m


def S(n: int) -> int:
    s = 1
    for i in range(1, n):
        s += D(i+1)
        s %= m
    # return (1 + sum([ D(i+1) for i in range(1, n) ])) % m
    # return (1 + sum([ D(i+1) for i in range(1, n) ]))
    return s % m

# scipy.special.comb(n, k)

# def Sl(n: int) -> int:
#     s = 1 # D(1) == 1
#     for i in range(2, n + 1):
#         # s += D(i+1)
#         p = 1
#         bnm1 = 1
#         for k in range(2, n + 1):

#     return s



print(B(1))
print(B(5))
print(D(5))
print(S(5))
print(S(10))
print(S(100) % m)
print(S(20000))

