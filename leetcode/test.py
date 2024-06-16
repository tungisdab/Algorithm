strs = ["alic3","bob","3","4","00000"]
ans = 0
for i in strs:
    x, y = 0, 0
    for j in i:
        print(j)
        if j.isalpha():
            x = 1
        elif j.isdigit():
            y = 0
    
    if x == 1 and y == 1:
        ans = max(ans, len(i))
    elif x == 0 and y == 1:
        ans = max(ans, int(i))
print(ans)
# return ans