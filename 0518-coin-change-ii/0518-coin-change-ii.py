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
        dp = [[-1]*(amount+1) for _ in range(n)]
        return self.f(n-1,amount,coins,dp)