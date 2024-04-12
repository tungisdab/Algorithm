words = ["Hello","Alaska","Dad","Peace"]
a = [ 'q','w','e','r','t','y','u','i','o','p', ]
b = [ 'a','s','d','f','g','h','j','k','l', ]
c = [ 'z','x','c','v','b','n','m', ]
ans = []
m = len(words)
for i in range(m):
    n = len(words[i])
    cc = 0
    if words[i][0].lower() in a:
        cc = 1
    if words[i][0] in b:
        cc = 2
    if words[i][0] in c:
        cc = 3
    print(words[i][0].lower())
    print(cc)
    k = 1
    for j in range(1, n):
        if cc == 1 and words[i][j] not in a:
            k = 0
            break
        if cc == 2 and words[i][j] not in b:
            k = 0
            break
        if cc == 3 and words[i][j] not in c:
            k = 0
            break
    if k == 1:
        ans.append(words[i]) 
print(*ans)
            

