nums = [2,1,4,3]
n = len(nums)
x = nums.index(1)
y = nums.index(2)
print(x, y)
k = x + (n - y - 1) if x < y else x + (n - y - 1) - 1
print(k)