class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        string_x = str(abs(x))[::-1]
        INT_MIN = -2**31      # -2147483648
        INT_MAX = 2**31 - 1   # 2147483647
        rev_x = sign * int(string_x)
        if INT_MIN < rev_x < INT_MAX:
            return rev_x
        else:
            return 0 