# import random

# c = 57307616
# n = 100000000
# for i in range(n, 10 * 10**7):
#     if i % 10**6 == 0:
#         print(i)
#     pp = sum([ random.randint(1,4) for i in range(9) ])
#     cc = sum([ random.randint(1,6) for i in range(6) ])
#     c += pp > cc
#     n += 1
# print(c, n, c / n)

# import scipy.special

# def point_sum(n: int, dice_size: int, no_dice: int):
#     # return scipy.special.comb(n - 1, no_dice - 1)
#     return (1 - )
cc = [
   0,    0,    0,    0,    0,    0,
   1,    6,   21,   56,  126,  252,
 456,  756, 1161, 1666, 2247, 2856,
3431, 3906, 4221, 4332, 4221, 3906,
3431, 2856, 2247, 1666, 1161,  756,
 456,  252,  126,   56,   21,    6,
   1]

pp = [
    0,     0,     0,     0,     0,     0,
    0,     0,     0,     1,     9,    45,
  165,   486,  1206,  2598,  4950,  8451, 
13051, 18351, 23607, 27876, 30276, 30276,
27876, 23607, 18351, 13051,  8451,  4950,
 2598,  1206,   486,   165,    45,     9,
    1]

c = 0
for i in range(36 + 1):
    for j in range(i+1, 36 + 1):
        c += pp[j] * cc[i]
print(c / (4**9 * 6**6))
# import itertools

# p = 4
# pp = [0]*40
# for i1 in range(1, p+1):
#     for i2 in range(1, p+1):
#         for i3 in range(1, p+1):
#             for i4 in range(1, p+1):
#                 for i5 in range(1, p+1):
#                     for i6 in range(1, p+1):
#                         for i7 in range(1, p+1):
#                             for i8 in range(1, p+1):
#                                 for i9 in range(1, p+1):
#                         # cc[i1+i2+i3+i4+i5+i6] += len(set(itertools.permutations([i1, i2, i3, i4, i5, i6])))
#                                     pp[i1+i2+i3+i4+i5+i6+i7+i8+i9] += 1
# print(pp)
    