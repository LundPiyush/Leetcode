class Solution:
    def subset(self,n,k,arr):
        '''
        prev =[False]*(k+1)
        cur =[False]*(k+1)
        prev[0]=cur[0] = True
        if arr[0]<=k:
            prev[arr[0]] = True
        '''
        dp=[[0]*(k+1) for _ in range(n)]
        for ind in range(0,n):
            dp[ind][0] = True
        
        if arr[0]<=k:
            dp[0][arr[0]] = True
        
        for ind in range(1,n):
            for target in range(k,-1,-1):
                not_take = dp[ind-1][target]
                take = False
                if arr[ind]<= target:
                    take = dp[ind-1][target-arr[ind]]
                dp[ind][target] = take or not_take
            #cur = prev
        return dp[n-1][k] 
        
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = 0
        n = len(nums)
        for i in range(len(nums)):
            total_sum += nums[i]
        if total_sum % 2 ==1:
            return False
        target = total_sum // 2
        return self.subset(n,target,nums)