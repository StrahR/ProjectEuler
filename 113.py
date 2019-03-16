memory = {
    (1, 1): 9,
    (2, 1): 8,
    (3, 1): 7,
    (4, 1): 6,
    (5, 1): 5,
    (6, 1): 4,
    (7, 1): 3,
    (8, 1): 2,
    (9, 1): 1
}

memory2 = {
    (1, 1): 2,
    (2, 1): 3,
    (3, 1): 4,
    (4, 1): 5,
    (5, 1): 6,
    (6, 1): 7,
    (7, 1): 8,
    (8, 1): 9,
    (9, 1): 10
}


def increasing(start: int, length: int) -> int:
    # print(start, length)
    if (start, length) in memory:
        return memory[(start, length)]
    c = 0
    for i in range(start, 10):
        c += increasing(i, length - 1)
    memory[(start, length)] = c
    return c


def decreasing(start: int, length: int) -> int:
    # print(start, length)
    if (start, length) in memory2:
        return memory2[(start, length)]
    c = 1
    for i in range(1, start + 1):
        c += decreasing(i, length - 1)
    memory2[(start, length)] = c
    return c


s = 0

for i in range(1, 10):
    for k in range(1, 100):
        s += increasing(i, k)
        s += decreasing(i, k)
        s -= 1  # double counted 555 for example
print(s + 9)  # add 9 for single digit numbers
