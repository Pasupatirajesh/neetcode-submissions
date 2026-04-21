class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0
        for i in range(len(prices)):
            while prices[i] < buy:
                buy = prices[i]

            if i != 0 and prices[i] > buy:
                profit = max(profit, prices[i]- buy)
        return profit
        