class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cnt = 0
        for i in hours:
            if i >= target:
                cnt += 1
        return cnt