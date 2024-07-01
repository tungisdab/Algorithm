emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
a = []
for i in emails:
    k = i.index('@')
    a.append(i[:k+1])
n = len(a)
for i in range(n):
    s = a[i].replace('.', '')
    a[i] = s
    k = a[i].count('+')
    if k == 1:
        x = a[i].replace('+', '')
        a[i] = x
    elif k >= 2:
        cc = 0
        x = ""
        for i in a[i]:
            if i == '+' and cc < 1:
                cc += 1
            else:
                x += i
        a[i] = x
ans = set(a)
print(ans)