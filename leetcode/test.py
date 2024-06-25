sentence = "a a ba"
a = [i for i in sentence.split()]
n = len(a)
x = a[0][-1]
for i in range(1, n):
    if x != a[i][0]:
        print(x, a[i][0])
        break
    print(x, a[i][0])
    x = a[i][-1]

if a[n-1][-1] != a[0][0]:
    print("kasf")

