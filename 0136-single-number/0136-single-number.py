class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for ele in nums:
            ans = ans ^ ele
        return ans