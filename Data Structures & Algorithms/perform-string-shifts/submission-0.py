class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        count = 0
        for direction, amount in shift:
                if direction == 0:
                    count-=amount
                elif direction == 1:
                    count+=amount
        netshift = count % len(s)
        return s[-netshift:] + s[:-netshift]

