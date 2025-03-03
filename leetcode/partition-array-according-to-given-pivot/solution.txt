class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a = []
        b = []
        c = []
        for i in nums:
            if i < pivot:
                a.append(i)
            elif i == pivot:
                b.append(i)
            else:
                c.append(i)
        ans = a + b + c
        return ans