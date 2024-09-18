n =7
x = bin(n).lstrip('-0b')
z = -1
for i in x:
    print(i, z)
    if (i == 1 and z == 1) or (i == 0 and z == -1):
        print("False") 
    z *= -1