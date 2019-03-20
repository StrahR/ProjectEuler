import scipy.special

_N = 70  # total balls
_n = 20  # balls picked
_k = 7   # number of colours
_b = 10  # number of balls in each colour

# _k = 2
# _b = 3
# _n = 3
# _N = _k*_b


def num(k):
    a = scipy.special.comb(_n-k + k-1, k-1, exact=True)  # stars and bars, for all possible combinations, with overdraw
    over = scipy.special.comb(_n-_b-1+1 - k + k-1, k-1, exact=True) * k  # how many ways to overdraw
    return a - over


def P(k):
    return num(k) / 195195


s = 0
nn = 0
for k in range(1, _k+1):
    s += int(scipy.special.comb(_k, k) * num(k)) ** 2
    nn += int(scipy.special.comb(_k, k) * num(k))
    print(k, s, nn)
# s *= scipy.special.factorial(20)
# print(round(s / scipy.special.comb(70, 20, exact=True), 8))
# print(round(s / (195195), 8))
# print(s)
# E(X) = sum(P(X)*N(X))
a = scipy.special.comb(_n + _k-1, _k-1, exact=True)  # stars and bars
over = scipy.special.comb(_n-_b-1 + _k-1, _k-1, exact=True) * 7  # stars and bars for overdraw
print(s / (a-over))
print(s / nn)
# print(nn)
