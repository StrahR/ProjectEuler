from strah import phi

# print(phi(9))
lim = 1000000
s = 0
for d in range(2, lim + 1):
    s += round(phi(d))
print(s)
