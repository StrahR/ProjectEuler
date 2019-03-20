from math import floor, sqrt, factorial


def sieve(n: int) -> list:
    '''Return list of primes up to `n`'''
    bit_field = [True] * n
    bit_field[0] = False
    bit_field[1] = False
    for i in range(2, floor(sqrt(n) + 1)):
        if bit_field[i]:
            for multiple_of_i in range(2 * i, n, i):
                bit_field[multiple_of_i] = False
    return [i for i in range(n) if bit_field[i]], bit_field


def is_prime(n: int) -> bool:
    '''Check if `n` is prime'''
    if n <= 1:  # 1 is neither prime nor composite
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, floor(sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def p(n: int) -> int:
    '''Return `n`-th prime number'''
    c = 0
    current = 1
    while c < n:
        current += 1
        if is_prime(current):
            c += 1
    return current


def pi(n: int) -> int:
    '''Number of primes less than `n`'''
    # Hardy & Wright formula
    # $\pi(n) = -1 + \sum_{j=3}^n \left((j-1)! mod j\right)$
    s = -1
    for j in range(3, n + 1):
        s += factorial(j - 2) % j
    return s


def is_composite(n: int) -> bool:
    '''Check if `n` is composite'''
    if n <= 1:  # 1 is neither prime nor composite
        return False
    if n == 2 or n == 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    for i in range(5, floor(sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return True
    return False


def digit_sum(n: int, f: "lambda or function?" = (lambda x: x)) -> int:
    '''Sum of the digits of `n` with given function'''
    return sum(map(f, map(int, list(str(n)))))


def divisors(n: int, proper: bool = False, prime: bool = False) -> list:
    '''
    Returns the list of (proper/prime) divisors of `n`.
    :param proper: Flag for proper divisors
    :return: Sorted list of divisors

    >>> divisors(6)
    [1, 2, 3, 6]
    >>> divisors(6, proper=True)
    [1, 2, 3]
    '''
    r = set()
    r.add(1)
    for i in range(2, floor(sqrt(n) + 1)):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    if not proper:
        r.add(n)
    return sorted(list(r))


def prime_factors(n: int) -> list:
    '''Returns the list of prime factors of n.

    >>> prime_divisors(2310)
    [2, 3, 5, 7, 11]
    '''
    r = set()
    while n % 2 == 0:
        r.add(2)
        n //= 2

    while n % 3 == 0:
        r.add(3)
        n //= 3

    for i in range(5, floor(sqrt(n)) + 1, 6):
        while n % i == 0:
            r.add(i)
            n //= i

        while n % (i + 2) == 0:
            r.add(i + 2)
            n //= (i + 2)

    if n > 2:  # if n is prime
        r.add(n)

    return sorted(list(r))


def phi(n: int) -> int:
    '''Euler's totient function'''
    factors = prime_factors(n)
    r = n
    for p in factors:
        r *= 1 - 1 / p
    return round(r)


from operator import mul
from functools import reduce


def rad(n: int) -> list:
    '''Radical of `n`'''
    return round(reduce(mul, prime_factors(n)))


def omega(n: int) -> int:
    '''Number of distinct prime factors'''
    return len(prime_factors(n))


def sigma(n: int, k: int = 1) -> int:
    '''Sum of `k`-th powers of divisors of `n`'''
    if n == 1:
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

        if n > 2:  # if n is prime
            r[n] += 1
        p = [i for i in range(n) if i]
        a = [r[i] for i in range(n) if i]
        prod = 1
        for i in range(1, len(p)):
            prod *= (p[i]**(a[i]+1) - 1) / (p[i] - 1)
        return int(prod)
    else:
        return sum(map((lambda d: d ** k), divisors(n)))


# add partiton function from 76, 77, 78

def reversed(n: int) -> int:
    '''Return `n` with digits reversed

    >>> reversed(123)
    321
    '''
    return int(str(n)[::-1])


def is_palindrome(n: int) -> bool:
    '''Test if `n` is palindromic'''
    return str(n) == str(n)[::-1]


def digits(n: int) -> list:
    '''Return the digits of `n`'''
    return sorted(map(int, list(str(n))))


def is_permutation(n: int, m: int) -> bool:
    '''Checks if `m` is a permutation of `n`'''
    return sorted(list(str(n))) == sorted(list(str(m)))


def is_pandigital(s: int, n: int = 9) -> bool:
    '''Check if number is `n`-digit pandigital'''
    return len(str(s)) == n and set(digits(s)) == set(range(1, n + 1))