class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)

        def memoization(i):
            if i <= 1:
                return 1
            if cache[i] != -1:
                return cache[i]
      
            cache[i] = memoization(i-1) + memoization(i-2)
            return cache[i]
        return memoization(n)
