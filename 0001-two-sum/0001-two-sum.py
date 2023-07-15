class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashing = {}
        for i in range(len(nums)):
            more = target - nums[i]
            if more in hashing:
                return [hashing[more],i]
            hashing[nums[i]] = i
        return {-1,-1}