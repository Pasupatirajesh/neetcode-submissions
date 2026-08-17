class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for d in details:
            ten = ord(d[11]) - ord('0')
            one = ord(d[12]) - ord('0')
            age = ten * 10 + one
            if age > 60:
                count+=1
        return count