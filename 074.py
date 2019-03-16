from strah import digit_sum
import math

mem = {}


def next_element(n: int) -> int:
    return digit_sum(n, math.factorial)


def factorial_chain_length(n: int) -> int:
    if n in mem:
        return mem[n]
    nn = next_element(n)
    if n == 169:
        ln = 3
    elif n == 871 or n == 872:
        ln = 2
    elif n == nn:
        ln = 1
    else:
        ln = 1 + factorial_chain_length(nn)
    mem[n] = ln
    return mem[n]


# print(factorial_chain_length(0))
# print(factorial_chain_length(1))
# print(factorial_chain_length(2))
# print(factorial_chain_length(3))
# print(factorial_chain_length(145))

c = 0
for n in range(10**6):
    if factorial_chain_length(n) == 60:
        c += 1
print(c)
