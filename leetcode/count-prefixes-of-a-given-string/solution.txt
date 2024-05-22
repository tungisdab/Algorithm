class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for i in words:
            if s.startswith(i):
                ans += 1
        return ans