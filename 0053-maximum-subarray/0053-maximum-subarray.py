class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        best_sum = nums[0]
        
        for element in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += element
            best_sum = max(best_sum,cur_sum)                                     
        
        return best_sum
            