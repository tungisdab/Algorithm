from collections import Counter


def digitCount(num):
    if len(str(num)) == 1:
        if num != 1:
            return False
        return True
    a = list(map(int, num))
    x = Counter(a)
    n = len(a)
    for i in range(n):
        if a[i] != x[i]:
            return False
    return True

num = "332"
print(digitCount(num))