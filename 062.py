# import itertools


# def is_cube(n: int) -> bool:
#     return round(n ** (1/3), 10) % 1 == 0


# n = 1200
# goal = 5
# while True:
#     # if n % 100 == 0:
#     print(n)
#     n += 1
#     s = str(n**3)
#     c = 1
#     for p in sorted(set(itertools.permutations(s)), reverse=True):
#         if ''.join(p) <= s or c > goal:
#             break
#         if is_cube(int(''.join(p))):
#             # print(''.join(p))
#             c += 1
#             if c == goal:
#                 print(n)
#     if c == goal:
#         print(s)
#         break
#     # print('-------------')

import math

breakpoints = [1, 10**(1/3), 100**(1/3), 1000**(1/3)]


mag = 0
goal = 3
goal = 5
while True:
    # print(mag)
    low =  math.floor(breakpoints[mag % 3    ] * 10**( mag    // 3))
    high = math.floor(breakpoints[mag % 3 + 1] * 10**(mag // 3)) + 1
    # print(low, high, mag)
    candidates = list()
    for i in sorted(range(low, high), reverse=True):
        l = sorted(list(str(i**3)))
        c = 1
        last = 0
        for k in sorted(range(low, i), reverse=True):
            if sorted(list(str(k**3))) == l:
                c += 1
                last = k
        if c == goal:
            print(last, last**3)
            candidates.append(last)
    if candidates:
        print(sorted(candidates)[0], sorted(candidates)[0] ** 3)
        break
    mag +=1








