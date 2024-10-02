# tokens = ["2","1","+","3","*"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
i = 2
for j in range(len(tokens)):
    if tokens[j] != '+' and tokens[j] != '-' and tokens[j] != '*' and tokens[j] != '/':
        tokens[j] = int(tokens[j])
while len(tokens) != 1:
    if tokens[i] == '+':
        x = tokens[i-1] + tokens[i-2]
        i -= 2
        tokens.pop(i)
        tokens.pop(i)
        tokens.pop(i)
        tokens.insert(i, x)
    elif tokens[i] == '-':
        x = tokens[i-2] - tokens[i-1]
        i -= 2
        tokens.pop(i)
        tokens.pop(i)
        tokens.pop(i)
        tokens.insert(i, x)
    elif tokens[i] == '*':
        x = tokens[i-1] * tokens[i-2]
        i -= 2
        tokens.pop(i)
        tokens.pop(i)
        tokens.pop(i)
        tokens.insert(i, x)
    elif tokens[i] == '/':
        x = tokens[i-2] // tokens[i-1]
        i -= 2
        tokens.pop(i)
        tokens.pop(i)
        tokens.pop(i)
        tokens.insert(i, x)
    i += 1
    print(tokens)
print(tokens[0])