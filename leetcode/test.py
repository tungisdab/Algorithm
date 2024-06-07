dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
ans = ""
dictionary.sort()
for i in sentence.split():
    x = ""
    for j in dictionary:
        if i.startswith(j):
            x = j
            print(x)
            break
    if x != "":
        ans += x
    else:
        ans += i
    ans += " "      
print(ans)