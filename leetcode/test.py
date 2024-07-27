# s = "Bob hit a ball, the hit BALL flew far after it was hit."
s = "a, a, a, a, b,b,b,c, c"
s = s.lower()
x = ''
for i in s:
    if i.isalpha() or i == ' ':
        x += i
    else: 
        x +=' '
x = list(x.split())
print(x)