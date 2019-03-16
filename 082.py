import math

a = list()

with open('p082_matrix.txt', 'r') as matrix:
    for row in matrix:
        row = row.replace('\n', '')
        a.append(list(map(int, row.split(','))))

w = len(a)
h = len(a[0])
a = [[a[i][j] for i in range(w)] for j in range(h)] # transpose

# a =[
# [131,201,630,537,805],
# [673,96,803,699,732],
# [234,342,746,497,524],
# [103,965,422,121,37],
# [18,150,111,956,331]]

w = len(a)
h = len(a[0])
candidate = list()
def value(i, j):
    if i < 0 or j < 0 or j >= h or i >= w:
        return math.inf
    else:
        return dist[i][j]

for i in range(h):
    dist = [[math.inf] * h for i in range(w)]
    dist[0][i] = a[0][i]


    # bellman-ford
    changed = True
    while changed:
        print('a')
        changed = False
        for i in range(w):
            for j in range(h):
                t = a[i][j] + min(
                    value(i-1, j  ),
                    value(i  , j+1),
                    value(i  , j-1),
                )
                if t < dist[i][j]:
                    dist[i][j] = t
                    changed = True
    candidate.append(min(dist[-1][j] for j in range(h)))
print(min(candidate))