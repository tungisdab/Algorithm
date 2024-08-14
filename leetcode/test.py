arr = [1,15,7,9,2,5,10]
k = 3
x = []
n = len(arr)
for i in range(n-k):
    x.append(max(arr[i:i+k]))
print(x)