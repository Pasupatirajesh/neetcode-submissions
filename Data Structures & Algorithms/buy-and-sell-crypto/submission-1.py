class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyp = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buyp:
                buyp = prices[i]
            profit = max(profit, (prices[i]- buyp))
        return profit