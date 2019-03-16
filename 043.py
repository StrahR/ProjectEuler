"""
d4 % 2 == 0
3 | d3 + d4 + d5
d6 = 5
d8 /in [1, 4]
d7 = d6 + d8
7 | d5d6d7
7 | 10*d5 - d6 + 2d8
"""

d1 = 0
d2 = 0
d3 = 0  #
d4 = 0  #
d5 = 0  #
d6 = 5  #
d7 = 0  #
d8 = 0  #
d9 = 0  #
d0 = 0  #
s = 0
for d4 in range(0, 10, 2):
    # d4 = i
    for d8 in range(1, 5):
        # if j == i:
        if d4 == d8:
            continue
        # d8 = j
        d7 = d6 + d8
        if d7 == d4:
            continue
        d9 = (13 - (100 * d7 + 10 * d8) % 13) % 13
        if d9 in (d4, d6, d7, d8):
            continue

        d0 = (17 - (100 * d8 + 10 * d9) % 17) % 17
        if d0 in (d4, d6, d7, d8, d9):
            continue

        r = (10 * d6 + d7) % 7
        t5 = (((7 if r % 2 == 1 else 0) - r) // 2) % 7  # 1/8, 2/9, 0/7
        for d5 in (t5, t5 + 7):
            if d5 > 9:
                break
            if d5 in (d4, d6, d7, d8, d9, d0):
                continue

            d3 = (3 - (d4 + d5) % 3) % 3
            if d3 in (d4, d5, d6, d7, d8, d9, d0):
                continue

            a1, a2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0} - {d3, d4, d5, d6, d7, d8, d9, d0}
            for d1, d2 in ((a1, a2), (a2, a1)):
                s += int(''.join(map(str, [d1, d2, d3, d4, d5, d6, d7, d8, d9, d0])))
print(s)
