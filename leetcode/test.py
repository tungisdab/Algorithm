n = 10
a = [1]
x, y, z = 1, 1, 1
while len(a) < n:
    x *= 2
    a.append(x)
    y *= 3
    a.append(y)
    z *= 5
    a.append(z)
print(a)