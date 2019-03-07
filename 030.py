from strah import digit_sum, digits

total = 0
for i in range(2, 1000000):
    s = digit_sum(i, (lambda d : d ** 5))
    if s == i:
        total += s
print(total)
