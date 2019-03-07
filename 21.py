from strah import divisors

def is_amicable(a: int) -> bool:
    b = sum(divisors(a, proper=True))
    return b != a and sum(divisors(b, proper=True)) == a


#print(is_amicable(220))
s = 0
for i in range(10000):
    if is_amicable(i):
        s += i
print(s)
