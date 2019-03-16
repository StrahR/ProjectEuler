a = 1
b = 2
c = 997

while True:
    if a ** 2 + b ** 2 == c ** 2:
        print(a * b * c)  # 31875000
        break
    b += 1
    c -= 1
    if b >= c:
        a += 1
        b = a + 1
        c = 1000 - a - b
