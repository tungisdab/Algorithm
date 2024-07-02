cost = [6,5,7,9,2,2]
n = len(cost)
a = sorted(cost, reverse = True)
ans = 0
for i in range(0, n-2, 3):
    ans += a[i] + a[i+1]
    print(a[i], a[i+1])
    print(ans)
x = n % 3
if x == 1:
    ans += a[n-1]
if x == 2:
    ans += a[n-2] + a[n-1]