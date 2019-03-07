from strah import is_palindrome

def is_lychrel(n: int) -> bool:
    for i in range(50):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False
    return True

c = 0
for n in range(1 ,10000):
    if is_lychrel(n):
        c += 1
print(c)
