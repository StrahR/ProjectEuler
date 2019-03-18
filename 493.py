import scipy.special

N = 70
n = 20


def num(k):
    '''precomputed with wolfram alpha
    https://math.stackexchange.com/questions/553960/extended-stars-and-bars-problemwhere-the-upper-limit-of-the-variable-is-bounded
    expand ((1-x^(r+1)))/(1-x))^n
    '''
    if k < 2:
        return 0
    # else:
    #     return scipy.special.comb(10*k-20 + k-1, k-1)

    if k == 2:
        return 1
    elif k == 3:
        return 63
    elif k == 4:
        return 633
    elif k == 5:
        return 3246
    elif k == 6:
        return 10872
    elif k == 7:
        return 26544
    else:
        return 0


s = 0

for k in range(1, 8):
    s += int(scipy.special.comb(7, k) * num(k)) ** 2
# s *= scipy.special.factorial(20)
print(round(s / scipy.special.comb(70, 20, exact=True), 8))
print(round(s / (195195), 8))
# print(s)
# E(X) = sum(P(X)*N(X))
