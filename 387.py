from strah import digit_sum, is_prime

harshad = list(range(1, 10))
right_truncatable_harshad = list(range(1, 10))


def is_harshad(n: int) -> bool:
    return n % digit_sum(n) == 0


# # while harshad:
# for j in range(13): # all right truncatable harshad numbers under 10**14
#     for h in harshad[:]:
#         for i in range(10):
#             n = 10 * h + i
#             if is_harshad(n):
#                 right_truncatable_harshad.append(n)
#                 harshad.append(n)
#         harshad.remove(h)
# # print(right_truncatable_harshad)

harshad = list(range(1, 10))
strong_harshad = list(range(1, 10))

for j in range(12):  # all strong, right truncatable harshad numbers under 10**14
    for h in harshad[:]:
        for i in range(10):
            n = 10 * h + i
            if is_harshad(n):
                if is_prime(n // digit_sum(n)):
                    strong_harshad.append(n)
                harshad.append(n)
        harshad.remove(h)
print(strong_harshad)

primes = list()
for h in strong_harshad:
    if h < 10:
        continue
    for i in (1, 3, 7, 9):
        n = 10 * h + i
        if is_prime(n):
            primes.append(n)
print(primes)
print(sum(primes))
