class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

        if not text1 or not text2:
            return 0
        
        def memo(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if text1[i] == text2[j]:
               dp[i][j]= 1 + memo(i+1, j+1)
               
            else:
                op1 = memo(i+1, j)
                op2 = memo(i, j+1)
                
                dp[i][j] = max(op1, op2)
            return dp[i][j]
        
        return memo(0, 0)
            
