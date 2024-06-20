s = "010"
a = list(s)
print(*a)
k = a.count('1')
a[-1] = '1'
k -= 1
i = 0
while k>=0:
    a[i] = '1'
    k -= 1
    i += 1
print(*a)