arr = [32,66,73,15,3,70,53]
pieces = [[66,73],[15],[3],[32],[70],[53]]
x = ''
for i in arr:
    x = x + str(i)
print(x)
for i in pieces:
    m = ''
    for j in i:
        m = m + str(j)
    
    if m not in x:
        # return False
        print('False')
    else:
        x = x.replace(m, 'z', 1)
    print(m, x)
# return True if x.isalpha() else False
print('True') if x.isalpha() else print('False')