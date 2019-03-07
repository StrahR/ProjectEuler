def is_increasing(n: int) -> bool:
    digits = list(str(n))
    return digits == sorted(digits)


def is_decreasing(n: int) -> bool:
    digits = list(str(n))
    return digits == sorted(digits, reverse=True)


def is_bouncy(n: int) -> bool:
    return not is_increasing(n) and not is_decreasing(n)


bouncy = 0
current = 1
while bouncy < current * 0.99:
    current += 1
    bouncy += is_bouncy(current)
print(bouncy, current, bouncy / current)
