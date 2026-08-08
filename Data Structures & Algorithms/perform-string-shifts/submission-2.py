class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shift_count = 0
        for direction, amount in shift:
            if direction == 0:
                shift_count-=amount
            elif direction == 1:
                shift_count+=amount
        netshift = shift_count % len(s)
        return s[-netshift:] + s[:-netshift]