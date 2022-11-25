class Solution:
    def maximumAdj(self,nums):
        n = len(nums)
        prev = nums[0]
        prev2 = 0
        for i in range(1,n):
            pick = nums[i]
            if i>1:
                pick+= prev2
            not_pick = 0 + prev
            curi = max(pick,not_pick)
            prev2 = prev 
            prev = curi
        return prev
    def rob(self, nums: List[int]) -> int:
        temp1 =[]
        temp2 =[]
        n = len(nums)
        if n ==1:
            return nums[0]
        for i in range(0,n):
            if i!=n-1:
                temp1.append(nums[i])
            if i!=0:         
                temp2.append(nums[i])
        return max(self.maximumAdj(temp1),self.maximumAdj(temp2))