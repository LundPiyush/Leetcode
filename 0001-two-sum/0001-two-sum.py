class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashing = {}
        for i in range(len(nums)):
            more = target - nums[i]
            if more in hashing:
                return [hashing[more],i]
            hashing[nums[i]] = i
        return {-1,-1}
    '''
        two pointer approach for Variant 2 where we have to tell pair is present yes or no
        nums.sort()
        n = len(nums)
        left,right = 0 , n-1
        # [2,3,4]
        while left <= right:
            if nums[left] + nums[right] < target:
                left+=1
            elif nums[left] + nums[right] > target:
                right-=1
            else:
                return "YES"
        return "NO"
    ''' 
        
    
        
    