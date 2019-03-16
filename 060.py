from strah import sieve, is_prime

end = 3
end = 4  # iterativno poglabljanje
# goal = 5

# bit_field = sieve(10 * 100**end)[1]
primes = sorted(sieve(10**end)[0], reverse=True)

mem = {}


def list_of_conc_primes(p1: int, primes1: list) -> list:
    primes2 = list()
    for p2 in primes1:
        if p2 <= p1:
            break
        if str((p1, p2)) in mem and mem[str((p1, p2))]:
            primes2.append(p2)
            continue
        p12 = int(str(p1) + str(p2))
        p21 = int(str(p2) + str(p1))
        # if bit_field[p21] and bit_field[p12]:
        if is_prime(p21) and is_prime(p12):
            mem[str((p1, p2))] = True
            primes2.append(p2)
        else:
            mem[str((p1, p2))] = False
    return primes2


print("start")
for p1 in primes:
    primes2 = list_of_conc_primes(p1, primes)
    for p2 in primes2:
        primes3 = list_of_conc_primes(p2, primes2)
        for p3 in primes3:
            primes4 = list_of_conc_primes(p3, primes3)
            # if primes4:
            #     l = [p1, p2, p3, primes4[-1]]
            #     print(l)
            #     s = sum(l)
            #     print(s)
            for p4 in primes4:
                primes5 = list_of_conc_primes(p4, primes4)
                if primes5:
                    ls = [p1, p2, p3, p4, primes5[-1]]
                    print(ls)
                    s = sum(ls)
                    print(s)
print(s)
