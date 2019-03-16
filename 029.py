exponents = set()
for a in range(2, 101):
    for b in range(2, 101):
        exponents.add(a**b)
print(len(exponents))  # 9183
