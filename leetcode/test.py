from collections import Counter


s = "ccccndxxlzerbsrrkvdnlvynxbjtjldsqgevphdlrldyishznryttvuratvwiafiwyjklafesvmcexuacxqgmnokfljxkystcbef"
target = "bvciovnpto"
x = Counter(s)
y = Counter(target)
m = float('inf')
z = set(target)
if len(z) == 1:
    i = target[0]
    if x[i] < y[i]:
        # return 0
        print(0)
    else:
        # return x[i] // y[i]
        print(x[i] // y[i])
for i in y:
    if x[i] == 0:
        print(0)
    else:
        if x[i] < y[i]:
            m = min(m, x[i])
        else:
            m = min(m, x[i] // y[i])
    print(m, i, x[i], y[i])
# return m