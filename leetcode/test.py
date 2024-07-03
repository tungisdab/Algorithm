path = "NNSWWEWSSESSWENNW"
x = [0, 0]
for i in path:
    if i == 'N':
        x[0] += 1
    elif i == 'S':
        x[0] -= 1
    elif i == 'E':
        x[1] += 1
    else: 
        x[1] -= 1
    print(x[0], x[1])
    if x[0] == 0 and x[1] == 0:
        print(1)
print(0)