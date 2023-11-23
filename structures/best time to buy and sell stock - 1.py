class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        min1 = prices[0]
        maxProfit = 0
        for i in range(size):
            if min1 > prices[i]: min1 = prices[i]
            currProfit = prices[i] - min1
            if maxProfit < currProfit: maxProfit = currProfit
        return maxProfit
        
