"""
 n  s k a_n
11 36 4 1679616
12 28 5 17210368
13 18 6 34012224
14 35 5 52521875
15 36 5 60466176
16 46 5 205962976
17 18 7 612220032
cp 17 : 1230000000?
"""

from strah import digit_sum as digsum

end = 30
n = 1230000000

for i in range(17, end + 1):
    while True:
        n += 1
        s = digsum(n)
        if s == 1:
            continue
        k = 2
        if n % 100000000 == 0:
            print("cp", i, s, n)
        while s ** k < n:
            k += 1
        if s ** k == n:
            print(i, s, k, n)
            break
