from math import floor, sqrt

def hypotenuse(a: int, b: int) -> int:
    c = sqrt(a * a + b * b)
    if c == floor(c):
        return c
    else:
        return None


mcount = 0
mp = 0
for p in range(3, 1001):
    count = 0
    for a in range(1, p // 2):
        for b in range(a, p):
            if a + b >= p:
                break
            c = hypotenuse(a, b)
            if c == None or a + b + c != p:
                continue
            #if a + b + sqrt(a * a + a * b + b * b) == p or a + b - sqrt(a * a + a * b + b * b) == p:
            count += 1
    if count > mcount:
        mcount = count
        mp = p
print(mp)

"""
0= p2 - 2p(a + b) + 2ab
p = (a + b) +- sqrt(a2 + b2 + ab)
"""
