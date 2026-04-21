class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins) + 1)]

        def memo(i, amount):
            if amount == 0: return 1
            if i >= len(coins) or amount < 0:
                return 0
            if dp[i][amount] != -1:
                return dp[i][amount]
            
            #This is skippin
            op1 = memo(i+1, amount)
            
            op2 = memo(i, amount - coins[i])
            dp[i][amount] = op1 + op2
            return dp[i][amount]
        return memo(0, amount)
    


