from strah import divisors


def is_abundant(n: int) -> bool:
    return sum(divisors(n, proper=True)) > n


def abundant_list(n: int) -> list:
    r = []
    for i in range(12, n + 1):
        if is_abundant(i):
            r.append(i)
    return r


def sums(nums: list) -> set:
    r = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            r.append(nums[i] + nums[j])
    return set(r)


n = 28123
nums = sums(abundant_list(n))
s = 0
for i in list(set(range(n+1)) - nums):
    s += i

print(s)
