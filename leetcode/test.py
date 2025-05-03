from collections import Counter
s = "2523533"
x = list(s)
a = Counter(x)
n = len(x)
for i in range(n-1):
    print(x[i], a[x[i]])
    print(x[i+1], a[x[i+1]])
    print('----------------')
    if x[i] == a[x[i]] and x[i+1] == a[x[i+1]]:
        print(str(x[i]) + str(x[i+1]))
