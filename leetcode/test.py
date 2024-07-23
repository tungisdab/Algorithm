s = "abcd"
x = list(s)
y = x[::-1]
n = len(x)
for i in range(n):
    if x[i] != y[i]:
        x[i] = min(x[i], y[i])
        y[i] = min(x[i], y[i])
print(x)
print(y)