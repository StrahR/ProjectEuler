from strah import sieve, is_prime

prime_list = sieve(87400)[0]

def number_of_primes(a: int, b: int) -> int:
    n = 2
    while is_prime(n ** 2 + a * n + b):
        n += 1
    return n - 1

# print("Start!")
m = 0
pr = 0
for b in prime_list:
    if b > 1000:
        break
    for a in range(1000):
        if not is_prime(a + b + 1):
            continue
        n = number_of_primes(a, b)
        if n > m:
            print(a, b)
            m = n
            pr = a * b
            break
        a = -a
        if not is_prime(a + b + 1):
            continue
        n = number_of_primes(a, b)
        if n > m:
            print(a, b)
            m = n
            pr = a * b
            break
print(pr)
