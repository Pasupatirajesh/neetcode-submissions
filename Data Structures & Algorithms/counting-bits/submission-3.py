class Solution:
    def countBits(self, n: int) -> List[int]:
        count = 0
        res = []
        for i in range(n+1):
            res.append(i.bit_count())
        return res
