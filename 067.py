grid = list()

with open("p067_triangle.txt") as triangle:
    for row in triangle:
        row = row.replace('\n', '')
        grid.append(list(map(int, row.split(' '))))

for i in range(len(grid)-2, -1, -1):
    for j in range(0, len(grid[i])):
        grid[i][j] += max(grid[i+1][j], grid[i+1][j+1])

print(grid[0][0])  # 7273
