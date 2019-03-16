from strah import is_palindrome

a = 999
b = 999
p = 0

while b > 99:
    if a * b > p and is_palindrome(a * b):
        p = a * b
    a -= 1
    if a < 100:
        a = 999
        b -= 1

print(p)
