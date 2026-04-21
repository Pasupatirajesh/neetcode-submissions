class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float('inf')
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if i !=0 and prices[i] > buy:
                sell = prices[i]
                profit = max(profit, (sell-buy))    
        return profit if profit > 0 else 0
        

