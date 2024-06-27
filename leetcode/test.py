def validPalindrome(s):
    if s == s[::-1]:
        return True
    a = list(s)
    x = a
    n = len(a)
    for i in range(n):
        a.pop(i)
        if a == a[::-1]:
            return True
        a = x
    return False

print(validPalindrome("abca"))