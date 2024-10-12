nums = [2,3,1,1,4]
n = len(nums)
i = 0
while i + nums[i] < n:
    m = max(nums[i:i+nums[i]+1])
    z = nums[i:i+nums[i]+1:-1]
    i += z.index(m)
    print(z)