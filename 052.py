from strah import digits

x = 1
while True:
    d = digits(2 * x)
    if d == digits(3 * x) and d == digits(4 * x) and d == digits(5 * x) and d == digits(6 * x):
        print(x)
        break
    x += 1
