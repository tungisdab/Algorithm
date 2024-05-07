num = int(input())
a = int(''.join(reversed(str(num))))
b = int(''.join(reversed(str(a))))
print(a+b)