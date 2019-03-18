from math import factorial
from strah import digit_sum
import time

print(digit_sum(145, factorial))
s = 0
for i in range(3, 10 ** 8):
    if i == digit_sum(i, factorial):
        s += i
        print(i)
print(s)
print(time.process_time())
