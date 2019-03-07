from strah import digit_sum

m = 0
for a in range(100):
    for b in range(100):
        m = max(m, digit_sum(a ** b))
print(m)
