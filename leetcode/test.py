nums = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]
n = len(nums)
i = 0
while i < n - 1:
    if nums[i] == nums[i+1]:
        nums[i] *= 2
        nums[i + 1] = 0
    i += 1
print(*nums)
ans = [0] * n
x = 0
for i in range(n):
    if nums[i]!= 0:
        ans[x] = nums[i]
        x += 1
print(*ans)