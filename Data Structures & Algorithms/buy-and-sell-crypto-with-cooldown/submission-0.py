class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        dp = {}

        def memo(i, cb):

            if i >= len(prices):
                return 0
            
            if (i, cb) in dp:
                return dp[(i, cb)]
            
            if cb:
                buy = memo(i+1, not cb) - prices[i]
                cooldown = memo(i+1, cb)
                dp[(i, cb)] = max(buy, cooldown)
            
            else:
                sell = memo(i+2, not cb) + prices[i]
                cooldown = memo(i+1, cb)
                dp[(i, cb)] = max(sell, cooldown)
            
            return dp[(i, cb)]
        
        return memo(0, True)
        
        