n = 5
x = bin(n)
x = x.lstrip('-0b')
print(x)
print(type(x))
a = []
for i in x:
    if x == '0':
        a.append('1')
    else:
        a.append('0')
print(a)
# return int(''.join(a), 2)
# print(int(''.join(a), 2))