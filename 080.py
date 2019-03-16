import decimal
from decimal import Decimal

decimal.getcontext().prec = 120


def digsum(n: int) -> int:
    return sum(map((lambda c: int(c)), list(str(n ** Decimal(1 / 2))[2:101]))) + int(n ** 0.5)


print(digsum(2))
print(int(99 ** 0.5))
s = 0
for i in range(1, 100):
    if i ** 0.5 % 1 == 0:
        # print(i)
        continue
    s += digsum(i)
print(s)
