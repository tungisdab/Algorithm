n = 5
ans = 0
for i in range(1, n-1):
    for j in range(i+1, n):
        x = (i*i + j*j) ** 0.5
        print(i, j, x)
        if x == int(x) and x <= n:
            ans += 1
print(ans)