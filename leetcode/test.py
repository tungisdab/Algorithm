s1 = "apple apple"
s2 = "banana"
s1 = [i for i in s1.split()]
s2 = [i for i in s2.split()]
s1 = set(s1)
s2 = set(s2)
print((s1 - s2) | (s2 - s1))