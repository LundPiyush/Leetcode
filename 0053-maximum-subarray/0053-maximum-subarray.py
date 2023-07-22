class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import sys
        maxi = -sys.maxsize-1
        sum =0
        n= len(nums) 
        for i in range(n):
            sum += nums[i]
            
            if sum >maxi:
                maxi = sum
            if sum<0:
                sum = 0
        return maxi