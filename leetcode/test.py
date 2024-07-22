s = "a0b1c2"
ans = ""
a = []
b = []
for i in s:
    if i.isdigit():
        a.append(i)
    else:
        b.append(i)
if abs(len(a) - len(b)) > 1:
    # return ''
    print('xxxxxxxxxxx')
print(a)
print(b)
if len(a) >= len(b):
    while len(a) == 0 and len(b) == 0:
        ans += a.pop()
        if b:
            ans += b.pop()
else:
    while len(a) == 0 and len(b) == 0:
        ans += b.pop()
        if a:
            ans += a.pop()
print(ans)