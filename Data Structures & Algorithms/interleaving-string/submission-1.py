class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n  = len(s1), len(s2)

        if len(s3) != m+n:
            return False
        dp = [[None for _ in range(n+1)] for _ in range(m+1)]

        def memo(i, j):
            if i+j == len(s3):
                return True 
            
            if dp[i][j] != None:
                return dp[i][j]
            ans = False
            if i < m and s1[i] == s3[i+j]:
                ans |= memo(i+1, j)
            
            if j < n and s2[j] == s3[i+j]:
                ans |= memo(i, j+1)
            
            dp[i][j] = ans
            return ans 
            
        return memo(0, 0)