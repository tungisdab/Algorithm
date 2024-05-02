class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        n = len(accounts)
        for i in range(n):
            ans = max(ans, sum(accounts[i]))
        return ans