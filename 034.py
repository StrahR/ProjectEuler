from math import factorial
from strah import digit_sum


print(digit_sum(145, factorial))
s = 0
for i in range(3, 10 ** 8):
    if i == digit_sum(i, factorial):
        s += i
print(s)
