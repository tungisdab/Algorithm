a = [2,5,3,4,1]
ans = 0
n = len(a)
for i in range(n, n-2):
    for j in range(i+1, n-1):
        print(a[i], a[j])

        if a[i] < a[j]:
            for k in range(j+1, n):
                if a[j] < a[k]:
                    ans += 1
                    print(a[i], a[j], a[k])
        elif a[i] > a[j]:
            for k in range(j+1, n):
                if a[j] > a[k]:
                    ans += 1
                    print(a[i], a[j], a[k])
