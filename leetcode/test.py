timeSeries = [1,2,3,4,5]
duration = 5
ans = 0
x = []
for i in timeSeries:
    x.append(i + duration - 1)
n = len(x)
print(timeSeries)
print(x)
for i in range(n-1):
    if timeSeries[i+1] > x[i]:
        ans += x[i] - timeSeries[i] + 1
    else:
        ans += timeSeries[i+1] - timeSeries[i]
        x[i] = timeSeries[i+1]
if timeSeries[n-1] > x[n-2]:
    ans += x[n-1] - timeSeries[n-1] + 1
else:
    ans += x[n-1] - x[n-2] + 1
print(ans)