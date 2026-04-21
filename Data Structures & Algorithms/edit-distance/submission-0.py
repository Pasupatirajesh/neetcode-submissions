class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def memo(i, j):

            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            

            if dp[i][j] != -1:
                return dp[i][j]
            
            count = 0
            if word1[i] == word2[j]:
                dp[i][j] = memo(i+1, j+1)
            else:
                op1 = memo(i, j+1)
                op2 = memo(i+1, j)
                op3 = memo(i+1, j+1)

                dp[i][j] = 1 + min(op1, op2, op3)
            return dp[i][j]
        return memo(0, 0)
