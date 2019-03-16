from strah import sigma

n = 0
c = 1
while not sigma(n, k=1) > 500:
    n += c
    c += 1
    # print(n)

print(n)  # 76576500
