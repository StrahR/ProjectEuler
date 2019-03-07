from math import floor,sqrt

def sieve(end):
    prime_list = []
    sieve_list = list(range(end))
    for i in range(2, end):
        if sieve_list[i]:
            prime_list.append(i)
            for mult in range(2 * i, end, i):
                sieve_list[mult] = 0
    return prime_list


n = 50000000
plist = sieve(floor(sqrt(n)) + 1)
numbers = []

for p2 in plist:
    for p3 in plist:
        n1 = p2 ** 2 + p3 ** 3
        if n1 > n:
            break
        for p4 in plist:
            n2 = n1 + p4 ** 4
            if n2 > n:
                break
            numbers.append(n2)
print(len(set(numbers)))
