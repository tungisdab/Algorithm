s = input()
n = len(s)
ans = 0
ans = 0
for i in range(1, n):
    a = s[:i]
    b = s[i:]
    a = a.count('0')
    b = b.count('1')
    ans = max(a+b, ans)
    print(a, b)
print(ans)