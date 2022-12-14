class Solution:
    def f(self,ind,T,arr,dp):
        if ind == 0:
            if T % arr[0] == 0:
                return 1
            else:
                return 0
        if dp[ind][T]!=-1:
            return dp[ind][T]
        not_take = self.f(ind-1,T,arr,dp)
        take = 0 
        if arr[ind]<=T:
            take = self.f(ind,T-arr[ind],arr,dp)
        dp[ind][T] = not_take + take
        
        return dp[ind][T]
    
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]
        #return self.f(n-1,amount,coins,dp) => recursion
        
        for T in range(0,amount+1):
            if T % coins[0]==0:
                dp[0][T] = 1
    
        for ind in range(1,n):
            for T in range(0,amount+1):
                not_take = dp[ind-1][T]
                take = 0 
                if coins[ind]<=T:
                    take = dp[ind][T-coins[ind]]
                dp[ind][T] = not_take + take
        return dp[n-1][amount]