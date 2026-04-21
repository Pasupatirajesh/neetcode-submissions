class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def memo(i, j):
            if i < 0 or  j < 0:
                return 0
            if i == m-1 or j == n-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]

            op1 = memo(i+1, j)
            op2 = memo(i, j+1)

            dp[i][j] = op1 + op2 

            return dp[i][j]
        return memo(0, 0)
        