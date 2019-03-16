from strah import digit_sum

numerator = 3
denominator = 2

f = lambda _: 1  # noqa: E731

c = 0
for i in range(1000):
    if digit_sum(numerator, f) > digit_sum(denominator, f):
        c += 1
    numerator, denominator = numerator + 2*denominator, numerator + denominator
print(c)
