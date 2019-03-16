from strah import sieve

target = 10**6
primes, bit_field = sieve(target)

# print(primes)

mlength = 0
mp = 0

s = 0
length = 0
for p in primes:
    if s+p > target:
        break
    s += p
    length += 1
# print(s, length, len(bit_field))

while True:
    for i in range(1, length):
        for j in range(i+1):
            t = s
            for k in range(j):
                t -= primes[k]  # subtract from the start
            for k in range(i-j):
                t -= primes[length - k - 1]  # subtract from the end
            # print('t:', t)
            if bit_field[t]:
                print(t, length-j)
                exit()


print(mp, mlength)

# for p in primes:
#     # print(p)
#     st = 0
#     length = 1
#     s = primes[0]
#     while s < p:
#         s += primes[st + length]
#         length += 1
#     while primes[st + length] < p:
#         while length <= mlength and st + length + 1 < len(primes):
#             length += 1
#             s += primes[st + length]
#         # print(s, length)
#         while s < p:
#             s += primes[st + length]
#             length += 1
#         if s == p:
#             if length > mlength:
#                 mlength = length
#                 mp = p
#                 # print(p, primes[st], st, length)
#             break

#         while s > p:
#             s -= primes[st]
#             st += 1
#             length -= 1
#         if s == p:
#             if length > mlength:
#                 mlength = length
#                 mp = p
#                 # print(p, primes[st], st, length)
#             break
# print(mp, mlength)
