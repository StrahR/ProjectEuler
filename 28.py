s = 1
c = 1
for step in range(2, 1001, 2):
    c += step
    s += c
    c += step
    s += c
    c += step
    s += c
    c += step
    s += c
print(s)
