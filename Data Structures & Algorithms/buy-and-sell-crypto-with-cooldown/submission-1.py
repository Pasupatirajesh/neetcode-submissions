class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n+2)]

        def memo(i, cb):
            if i >= n:
                return 0
            
            if dp[i][cb] != -1:
                return dp[i][cb]
            
            if cb:
                buy = memo(i+1, 0) - prices[i]
                cooldown = memo(i+1, 1)
                dp[i][cb] = max(buy, cooldown)
            else:
                sell = memo(i+2, 1) + prices[i]
                cooldown = memo(i+1, 0)
                dp[i][cb] = max(sell, cooldown)
            return dp[i][cb]
        
        return memo(0, 1)
            

    