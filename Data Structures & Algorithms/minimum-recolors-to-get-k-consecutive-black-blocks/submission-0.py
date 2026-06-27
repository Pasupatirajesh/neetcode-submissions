class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, 0
        count = 0
        res = 0
        for i in range(k):
            if blocks[i] == 'W':
                count+=1
        res = count
        for i in range(k, len(blocks)):
            if blocks[i-k] == "W":
                count-=1
            if blocks[i] == "W":
                count+=1
            res = min(res, count)
        return res