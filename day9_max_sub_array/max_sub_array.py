'''
Problem - https://leetcode.com/problems/maximum-subarray
Solution - https://www.youtube.com/watch?v=2ln84zDGIhI
'''

def maxSubArray(self, nums: List[int]) -> int:
    maxSoFar = nums[0]
    maxSum=nums[0]
    for i in range(1,len(nums)):
        if maxSoFar < 0:
            maxSoFar = 0
        maxSoFar += nums[i]
        maxSum= max(maxSum,maxSoFar)
    return maxSum
