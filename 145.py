def is_reversible(n: int) -> bool:
    return all(map((lambda c: int(c) % 2 == 1), list(str(n + int(str(n)[::-1])))))


print(is_reversible(63), is_reversible(62))

c = 0
target = 10 ** 9
for i in range(1, target, 2):
    if i % 10000000 == 1:
        print('{0:3}%: {1:10}'.format(i // 10000000, c))
    if is_reversible(i):
        c += 2
print(c)
