s = 0
for n in range(1, 1000000):
    b = bin(n)[2 :]
    if str(n) == str(n)[:: -1] and b == b[:: -1]:
        s += n
print(s)
