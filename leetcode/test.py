code = [2,4,9,3]
k = -2
n = len(code)
# if k == 0:
#     return [0] * n
a = code + code
ans = []
if k < 0:
    for i in range(n, 2 * n):
        ans.append(sum(a[i - k - 1:i]))
    print(ans)
else:
    for i in range(0, n):
        ans.append(sum(a[i + 1:i+k+1]))
# return ans