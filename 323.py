import scipy.special

E = [0]
# dynamic programming
for n in range(1, 33):
    e = (1 + sum([(1 + E[k]) * scipy.special.comb(n, k) for k in range(n)])) / (2**n-1)
    E.append(e)
# print(E)
print(round(E[32], 10))
