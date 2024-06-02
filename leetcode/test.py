start = 3
goal = 4
a = bin(start)
b = bin(goal)
a = a.lstrip('-0b')
b = b.lstrip('-0b')
print(a, b)
while len(a) < len(b):
    a = '0' + b
while len(a) > len(b):
    b = '0' + b
print(a, b)
n = len(a)
ans = 0
for i in range(n):
    if a[i] != b[i]:
        ans += 1
print(ans)