from math import sqrt, lcm
from decimal import *
getcontext().prec = 1000000000

def F(n: int) -> int:
    return round(Decimal((Decimal(5 ** Decimal(0.5) + 1) / 2) ** n) / Decimal(5 ** Decimal(0.5)))


def pi(m: int) -> int:
    '''Returns pisano period for m'''
    a = 0
    b = 1
    for i in range(1, 6 * m):
        c = (a + b) % m
        a = b
        b = c
        if (a, b) == (0, 1):
            return i
    return(-1) # should not reach here

#print(pi(3))

mask = 1234567891011
#pim = pi(mask)
pim = 900788112 # computed by above function. Took a minute.

#import numpy as np
#print(np.lcm.reduce([pi(3), pi(7), pi(13), pi(67), pi(107), pi(630803)]))

#print(pim)
#import datetime
#print(datetime.time())
#print(F(10**14 % pim))
#print(datetime.time())




