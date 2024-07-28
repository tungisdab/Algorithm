s = "ab"
n = len(s)
# if n < 2:
#     return False
for i in range(1, n // 2 + 2):
    if n % i == 0:
        x = s[:i]
        a = x * (n // i)
        if a == s:
            print(a, s)