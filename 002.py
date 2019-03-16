i = 1
j = 2
s = 2

while True:
    for _ in range(3):  # vsak tretji bo sod, pazimo da začnemo na pravem mestu
        t = i + j
        i = j
        j = t
    if j > 4000000:
        break
    s += j
print(s)
