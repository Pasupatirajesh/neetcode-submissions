class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [-1] * (amount + 1)

        def memo(amount):
            if amount < 0:
                return float("inf")
            if amount == 0:
                return 0
            if dp[amount] != -1:
                return dp[amount]
            
            min_coin = float("inf")
            for coin in coins:
                min_coin = min(min_coin, 1+ memo(amount -coin))
            
            dp[amount] = min_coin
            return dp[amount]
        
        res = memo(amount)
        return res if res != float("inf") else -1