class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        if len(details) == 0:
            return 0
        
        for detail in details:
            detail = detail[11:13]
            detail = int(detail)
            if detail > 60:
                count+=1
        return count