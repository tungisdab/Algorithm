a = [3,4,1,2]
k = 25
n = len(a)
i = 0
while a[i] > k:
    k -= a[i]
    i += 1
    if i == n:
        i = 0
    print(i, k)