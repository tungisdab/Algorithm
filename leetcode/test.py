
def check(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i:
            return False
    return True

for i in range(990, 1049):
    x = bin(i)
    k = x.count('1')
    if check(k):
        print(k, i)