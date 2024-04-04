n = int(input())
n = str(n)
print(n)
m = len(n)
x = ''.join(reversed(n))
print(x)
a = 0
for i in range(m):
    a += (int(x[i]) * 2**(m-i-1))
print(a)