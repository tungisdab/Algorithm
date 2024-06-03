words = ["abc","car","ada","racecar","cool"]
for i in words:
    x = ''.join(reversed(i))
    print(i)
    print(x)
    if x == i:
        print(i) 