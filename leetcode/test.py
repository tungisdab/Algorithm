s = "abcd"
k = 2
n = len(s)
x = 0
ans = ''
tmp = 0
for i in range(n):
    if i == n-1:
        ans += chr(tmp % 26 + ord('a'))
    if x == k:
        x = 0
        ans += chr(tmp % 26 + ord('a'))
        tmp = 0
    tmp += ord(s[i]) - ord('a')
    x += 1
    print(tmp)
print(ans)