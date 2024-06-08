m = 2
n = 3
indices = [[0,1],[1,1]]
a = [[0] * n] * m
for i, j in indices:
    for x in range(n):
        a[i][x] = a[i][x] + 1
    for x in range(m):
        a[x][j] = a[x][j] + 1
print(*a)
ans = 0
for i in a:
    for j in i:
        if j%2:
            ans += 1
print(ans)