from strah import is_prime
from math import floor, sqrt

n = 31
while True:
    n += 2
    #print(n)
    if is_prime(n):
        continue
    b = False
    for p in range(2, n):
        if not is_prime(p):
            continue
        # for k in range(1, floor(sqrt((n - p) // 2)) + 1): # could only try one value
        k = floor(sqrt((n - p) // 2))
        if p + 2 * k ** 2 == n:
            b = True
    if not b:
        print(n)
        break
