'''
121. Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock
https://www.youtube.com/watch?v=eMSfBgbiEjk
'''


def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        
        for i in range(1,len(prices)):
            min_price = min(min_price,prices[i])
            profit = max(profit, prices[i]-min_price)
            
        return profit