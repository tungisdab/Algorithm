nums1 = [int(i) for i in input().split()]
m = int(input())
nums2 = [int(i) for i in input().split()]
n = int(input())
a = []
for i in range(m):
    a.append(nums1[i])
for i in range(n):
    a.append(nums2[i])
a.sort()
nums1 = [int(i) for i in a]
print(*nums1)