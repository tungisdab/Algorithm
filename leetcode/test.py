bills = [5,5,5,10,20]
x = {5: 0, 10: 0, 20: 0}
for i in bills:
    if i == 5:
        x[5] += 1
    elif i == 10:
        if x[5] == 0:
            # return False
            print('1')
        else:
            x[5] -= 1
    else:
        if x[10]:
            if x[5] == 0:
                # return False
                print('2')
            x[10] -= 1
            x[5] -= 1
        else:
            
            if x[5] < 3:
                # return False
                print('3')
            x[5] -= 3