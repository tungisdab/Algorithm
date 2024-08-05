apple = [9,8,8,2,3,1,6]
capacity = [10,1,4,10,8,5]
k = sum(apple)
print(k)
a = sorted(capacity, reverse = True)
x = 0
n = len(a)
for i in range(n):
    x += a[i]
    print(x)
    if x > k:
        print(i+1)
print(n)