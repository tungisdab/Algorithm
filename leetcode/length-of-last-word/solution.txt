class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = [str(i) for i in s.split()]
        return len(arr[len(arr) - 1])