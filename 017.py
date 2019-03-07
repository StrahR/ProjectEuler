letter_count = {
0 : 0,
1 : 3,
2 : 3,
3 : 5,
4 : 4,
5 : 4,
6 : 3,
7 : 5,
8 : 5,
9 : 4,
10 : 3,
11 : 6,
12 : 6,
13 : 8,
14 : 8,
15 : 7,
16 : 7,
17 : 9,
18 : 8,
19 : 8,
20 : 6,
30 : 6,
40 : 5,
50 : 5,
60 : 5,
70 : 7,
80 : 6,
90 : 6
}

c = 3 + 8 # one thousand
for n in range(1, 20):
    c += letter_count[n]
for n in range(20, 1000):
    if n < 100:
        c += letter_count[10 * (n // 10)] + letter_count[n % 10]
    elif n % 100 == 0:
        c += letter_count[n // 100] + 7 # ___ hundred
    else: # n < 1000
        c += letter_count[n // 100] + 7 + 3 # ___ hundred and
        if n % 100 < 20:
            c += letter_count[n % 100]
        else:
            c += letter_count[10 * ((n % 100) // 10)] + letter_count[n % 10]

print(c) # 21124








