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
        dp=[-1]*n
        return self.f(n-1,nums,dp)