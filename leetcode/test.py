x = int(input())
y = int(input())
x = bin(x)
a = x.lstrip('-0b')
y = bin(y)
b = y.lstrip('-0b')
print(a, b)
ans = 0
n = len(a) - 1
m = len(b) - 1
print(n, m)
while n >= 0 and m >=0:
    if a[n] != b[m]:
        ans += 1
    n -= 1
    m -= 1
print(ans)
