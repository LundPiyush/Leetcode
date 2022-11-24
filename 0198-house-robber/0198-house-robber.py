class Solution:
    def f(self,ind,nums,dp):
        if ind<0:
            return 0
        if ind==0:
            return nums[0]
        if dp[ind]!=-1:
            return dp[ind]
        pick = nums[ind] + self.f(ind-2,nums,dp)
        not_pick = 0 + self.f(ind-1,nums,dp)
        dp[ind]=max(pick,not_pick)
        return dp[ind]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        #tabulation : 
        # space optimization store prev = dp[i-1]  and prev2 = dp[i-2]  
        prev , prev2 , curi = 0,0,0
        for i in range(0,n):
            if i==0:
                dp[i] = nums[0]
            pick = nums[i]
            if i>1:
                pick += dp[i-2] # pick element and move back by 2
            not_pick = 0 + dp[i-1] # not picked so don't add anything and move back by 1
            
            dp[i]=max(pick,not_pick)
        return dp[n-1]
        #return self.f(n-1,nums,dp) => recursion solution with memoziation