class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyp = prices[0]
        sellp = 0
        for i in range(1, len(prices)):
            if prices[i] < buyp:
                buyp = prices[i]
            sellp = max(sellp, prices[i]-buyp) 
        return sellp       