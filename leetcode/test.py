num1 = "1+-1i"
num2 = "0+0i"
num1 = num1.replace('i', '')
num2 = num2.replace('i', '')
a, b = num1.split('+')
c, d = num1.split('+')
a = int(a)
b = int(b)
c = int(c)
d = int(d)
print(a, b, c, d)
ans = str(a * c - b * d) + '+' + str(a * d + b * c) + 'i'
print(ans)