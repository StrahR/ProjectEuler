import math
from math import sqrt, floor
from decimal import *
# getcontext().prec = 1000

# def F(n: int) -> int:
#     return round(Decimal(Decimal(Decimal(5 ** Decimal(0.5) + 1) / 2) ** n) / Decimal(5 ** Decimal(0.5)))
def F(n: int) -> int:
    phi = (1 + 5 ** Decimal(.5)) / 2
    getcontext().prec = floor(n * math.log10(phi) - math.log10(5) / 2) + 25

    return round(Decimal(phi ** n) / Decimal(5 ** Decimal(0.5)))

#n = F(3890)
#print(len(set(str(n // (10 ** (len(str(n)) - 9))))))
#print(len(set(str(n % 10 ** 9))))

def is_good(n: int) -> bool:
    #f = F(n)
    f = n
    f9 = (f // (10 ** (len(str(f)) - 9))) * 10
    l9 = (f % 10 ** 9) * 10
    return len(set(str(f9) + '0')) == 10 and len(set(str(l9) + '0')) == 10




#print(len(str(F(3890))))

#k = 2745
#while not is_good(k):
    #k += 1
#print(k)

a = F(2749)
b = F(2750)
c = 2750
while not is_good(F(c)):
    c += 1
    # t = a
    # a = b
    # b = t + b
print(c)
