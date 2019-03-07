def count(n: int, m: int) -> int:
    #s = 0
    #for i in range(1, n + 1):
        #for j in range(1, m + 1):
            #s += i * j
    #return s
    return round(m * (m + 1) * n * (n + 1) / 4) # courtesy of Wolfram Alpha


#print(count(1,1999))

target = 2000000
area = 2000
mdist = 1000
for i in range(1, 2000):
    for j in range(1, 2000):
        c = count(i, j)
        if abs(c - target) < mdist:
            mdist = abs(c - target)
            area = i * j
print(area)
