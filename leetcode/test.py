left = 5
right = 7
print(bin(left), bin(right))
cnt = 0
while left != right:
    left >>= 1
    right >>= 1
    cnt += 1
    print(left, right)
    print(bin(left), bin(right))
print(left, bin(left))
print(left << cnt, bin(left << cnt))