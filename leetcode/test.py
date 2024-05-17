word = 'aaAbcBC'
a = {str(i) for i in word if i < 'z' and i > 'a'}
b = {str(i) for i in word if i < 'Z' and i > 'A'}
print(a, b)
ans = 0
for i in a:
    if i.upper() in b:
        ans += 1
# return ans
print(ans)