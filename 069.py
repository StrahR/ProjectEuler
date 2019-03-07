from strah import phi

target = 1000000
mnphi = 0
mn = 0
for n in range(1, target + 1):
    # if n % 100000 == 0:
    #     print(n)
    nphi = n / phi(n)
    if nphi > mnphi:
        mnphi = nphi
        mn = n
print(mn)
