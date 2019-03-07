l = dict()
for a in range(2, 101):
    for b in range(2, 101):
        l[a**b] = 1
print(len(l)) # 9183