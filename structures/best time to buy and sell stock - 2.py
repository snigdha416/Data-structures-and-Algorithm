class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        max1 = prices[size - 1]
        maxProfit = 0
        for i in range(size - 1, -1, -1):
            if max1 < prices[i]: max1 = prices[i]
            currProfit = max1 - prices[i]
            if maxProfit < currProfit: maxProfit = currProfit
        return maxProfit
        
