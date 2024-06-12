strs = ["abc", "bce", "cae"]
n = len(strs)
m = len(strs[0])
a = []
for i in range(m):
    x = []
    for j in range(n):
        x.append(strs[j][i])
    a.append(x)
ans = 0
for i in a:
    x = i
    x.sort()
    print(i, x)
    if x != i:
        ans += 1