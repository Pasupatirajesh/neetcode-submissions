class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def memo(i, j):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            
            dp[i][j] = memo(i+1, j) + memo(i, j+1)
            
            return dp[i][j]
        return memo(0, 0)