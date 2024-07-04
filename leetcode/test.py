s = "lEetcOde"
x = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
a = list(s)
b = [i for i in a if i in x]
print(b)
n = len(b)
for i in range(n-1):
    for j in range(i+1, n):
        if b[i] > b[j]:
            b[i], b[j] = b[j], b[i]
print(b)
z = 0
for i in range(len(a)):
    if i in x:
        a[i] = b[z]
        z += 1
print(''.join(a))