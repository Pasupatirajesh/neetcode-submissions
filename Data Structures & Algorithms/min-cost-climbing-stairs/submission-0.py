class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) 
        dp = [-1] * (n+1)

        def memo(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] +  min(memo(i+1), memo(i+2))
            return dp[i]
        
        return min(memo(0), memo(1))
