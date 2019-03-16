from strah import rad

"""
from operator import mul
from functools import reduce

def rad(n: int) -> list:
    r = []
    while n % 2 == 0:
        r.append(2)
        n /= 2

    while n % 3 == 0:
        r.append(3)
        n /= 3

    for i in range(5, floor(sqrt(n)) + 1, 6):
        while n % i == 0:
            r.append(i)
            n /= i

        while n % (i + 2) == 0:
            r.append(i + 2)
            n /= (i + 2)

    if n > 2:
        r.append(n)

    return round(reduce(mul, set(r)))
"""

nums = [(1, 1)]
for i in range(2, 100001):
    nums.append((rad(i), i))
print(sorted(nums)[9999])
