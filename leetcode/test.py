operations = ["5","-2","4","C","D","9","+","+"]
ans = []
for i in operations:
    if i.isdigit():
        ans.append(int(i))
    if i == "C":
        ans.pop()
    if i == "D":
        ans.append(ans[-1] * 2)
    if i == "+":
        ans.append(ans[-1] + ans[-2])
    print(ans)
print(sum(ans))