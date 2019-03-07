def sq_digsum(n: int) -> int:
    return sum(map((lambda n: int(n) ** 2), list(str(n))))


print(sq_digsum(89))

memory = {}
target = 10000000
c = 0
mem = 0
for n in range(1, target):
    memory[n - 1] = mem
    if n % 100000 == 0:
        print(n)
    while True:
        n = sq_digsum(n)
        if n in memory:
            c += memory[n]
            break
        if n == 1:
            mem = 0
            break
        if n in (89, 85, 145, 20, 4, 16, 37, 58):
            mem = 1
            c += 1
            break
print(c)
