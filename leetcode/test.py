nums = [10,10,3,7,6]
ans = 0
s = sum(nums)
a = nums[0]
for i in range(1, len(nums)):
    x = s - a
    print(a, x, ans)
    if (a - x) % 2 == 0:
        ans += 1
    a += nums[i]
print(ans)