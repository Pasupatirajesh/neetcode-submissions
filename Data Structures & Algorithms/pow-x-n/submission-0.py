class Solution:
    def myPow(self, x: float, n: int) -> float:

        def recurse(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = recurse(x, n // 2)
            res = res * res
            return res * x if n % 2 else res
            
        res = recurse(x, abs(n))
        return 1 / res if n < 0 else res