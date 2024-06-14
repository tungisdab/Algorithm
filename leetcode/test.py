s = "xyzzaz"
cnt = 0
n = len(s)
for i in range(0, n-2):
    if len(s[i:i+3]) == len(set(s[i:i+3])):
        cnt += 1
        print(s[i:i+2])
print(cnt)