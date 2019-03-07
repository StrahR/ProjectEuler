def cycle_len(d: int) -> int:
    # Če je `n` perioda števila `d`, potem ima `(10 ** n - 1) / d` končen decimalni zapis,
    # ki pa bo imel kvečjemu n decimalk.
    n = 1
    while (10 ** n) * (10 ** n - 1) % d != 0: # hackedy hack hack
        n += 1
    return n


n = 1000
c = 0
m = 0
for i in range(2, n):
    c = cycle_len(i)
    if m < c:
        m = c
        d = i
print(d)
