pattern = "acdcbbb"
n = len(set(pattern))
k = 0
cc = ''
x = []
for i in pattern:
    if i not in x:
        cc = cc + str(k)
        x.append(i)
        k += 1
    else:
        cc = cc + str(x.index(i))
print(cc)