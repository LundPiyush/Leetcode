class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        n=len(prices)
        
        for i in range(n):
            cost = prices[i] - mini
            profit =max(profit,cost)
            mini=min(mini,prices[i])
        return profit