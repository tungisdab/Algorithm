s = "erase*****"
a = list(s)
n = len(s)
i = 0
while i < n:
    if a[i] == "*":
        j = i -1
        while j >= 0:
            if a[j] != "*":
                del a[j]
                n -= 1
                i -= 1
                break
            else:
                j -= 1
        del a[i]
        n -= 1
        i -= 1
    i += 1
    print(''.join(a))
print(''.join(a))
