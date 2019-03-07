from strah import sieve, is_permutation

prime_list = sieve(10000)

for p in prime_list:
    if p < 1000:
        continue
    for d in range(1, (10000 - p) // 2): # i + 2 * d > 10000
        if (p + d) not in prime_list or (p + 2 * d) not in prime_list:
            continue
        if is_permutation(p, p + d) and is_permutation(p, p + d + d):
            print(p, p + d, p + d + d, str(p) + str(p + d) + str(p + d + d))
