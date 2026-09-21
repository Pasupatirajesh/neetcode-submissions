class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        res = 0
        sign = -1 if x < 0 else 1 
        x = abs(x)
        while x > 0:
            digit_x = x % 10
            res = res * 10 + digit_x
            x = x // 10 
        if res > MAX or res < MIN:
            return 0
        else:
            return sign * res 