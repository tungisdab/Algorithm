grid = [[1,0],[0,2]]
x, y, z = 0, 0, 0
for i in grid:
    for j in i:
        x += 1
    y += max(i)
n = len(grid)
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp = max(tmp, grid[j][i])
    z += tmp
print(x, y, z)