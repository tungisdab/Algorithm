num1 = input()
num2 = input()
while len(num1) < len(num2):
    num1 = '0' + num1
while len(num2) < len(num1):
    num2 = '0' + num2
n = len(num1)
s = ''
cc = 0
print(num1)
print(num2)
while n >= 0:
    n -= 1
    if cc == 0:
        s = str((int(num1[n]) + int(num2[n])) % 10) + s
        print(s)
        if (int(num1[n]) + int(num2[n]))  >= 10:
            cc = 1
        else:
            cc = 0
    else:
        s = str((int(num1[n]) + 1 + int(num2[n])) % 10) + s
        print(s)
        if (int(num1[n]) + 1 + int(num2[n]))  >= 10:
            cc = 1
        else:
            cc = 0
if cc == 1:
    s = '1' + s
print(s)
    
