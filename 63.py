import math

# # naive
# def under_(n: int) -> int:
#     '''How many n-digit positive integers exist which are also an nth power'''
#     c = 0
#     for i in range(10**n // 10, 10**n):
#         # for k in range(10**i):
#         k = math.floor(i**(1/n))
#         if k**n < i:
#             continue
#         if k**n > i:
#             break
#         c += 1
#         print(i, k, n)
#     return c

# print(under_(9))

end = 10**3
c = 0
for k in range(1, end):
    for i in range(1, end):
        if len(str(k**i)) < i:
            continue
        if len(str(k**i)) > i:
            break
        c += 1
print(c)




