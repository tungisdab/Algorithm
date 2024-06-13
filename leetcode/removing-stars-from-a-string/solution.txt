class Solution:
    def removeStars(self, s: str) -> str:
        a = []
        for i in s:
            if i == '*':
                a.pop()
            else:
                a.append(i)
        return ''.join(a)