s = "abacaba"
ans = 0
x = set()
for i in s:
    if i not in x:
        x.add(i)
    else:
        x.clear()
        ans += 1
    print(x)
    print(ans)