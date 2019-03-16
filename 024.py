import itertools
p = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(''.join(map(str, p[999999])))  # 2783915460
