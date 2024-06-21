class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for i in details:
            if int(i[11:13]) > 60:
                cnt += 1
        return cnt