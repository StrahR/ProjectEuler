def sq_digsum(n: int) -> int:
    return sum(map((lambda n: int(n) ** 2), list(str(n))))


memory = { 1: False, 44: False, 32: False, 13: False, 10: False,
          89: True, 85: True, 145: True, 20: True, 4: True, 16: True, 37: True, 58: True }


def ends_in_89(n: int) -> bool:
    if n in memory:
        return memory[n]
    b = ends_in_89(sq_digsum(n))
    memory[n] = b
    return b


target = 10000000
c = 0
for n in range(1, target):
    c += ends_in_89(n)
print(c)
