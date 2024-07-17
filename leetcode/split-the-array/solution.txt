class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return all(i <= 2 for i in Counter(nums).values())