class Solution:
    def f(self,ind,T,coins,dp):
    #base case
        if ind == 0 :
            if T % coins[0]==0: 
                return T//coins[0]
            else:
                return float('inf')
        # target is 12 and coins[0] is 4 so ans will be 3 (12/4). you will take three coins of 4 to get 12 as target
        # if target is 7 and coins[0] is 6 . 0 coins will be added in ans , bcz you cannoyt form target =7 with coins[0]=6
        
        if dp[ind][T]!=-1:
            return dp[ind][T]
        not_take = 0 + self.f(ind-1,T,coins,dp)
        take = float('inf')
        if coins[ind]<=T:
            take = 1 + self.f(ind,T-coins[ind],coins,dp)
        dp[ind][T] = min(not_take,take)
        return dp[ind][T]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp =[[-1]*(amount+1) for _ in range(n)]
    #recursion
        out = self.f(n-1,amount,coins,dp)
        if out == float('inf'):
            return -1
        return out
    
        