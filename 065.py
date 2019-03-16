from strah import digit_sum

mem = {0: 1, 1: 1, 2: 2}


def numerator(n: int) -> int:
    '''OEIS A113873'''
    # if n < 3:
    #     return n or 1
    # else:
    if n in mem:
        return mem[n]
    # if n % 3 == 0:
    #     mem[n] = numerator(n - 1) + numerator(n - 2)
    if n % 3 == 1:
        mem[n] = 2 * (n//3) * numerator(n - 1) + numerator(n - 2)
    else:
        mem[n] = numerator(n - 1) + numerator(n - 2)
    return mem[n]


print(digit_sum(numerator(101)))
