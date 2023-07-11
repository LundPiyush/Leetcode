class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = -1 
        for  i in range(n):
            if nums[i] == 0:
                j=i
                break
        # no zero found in array
        if j == -1:
            return nums
        
        for i in range(j+1,n,1):
            if nums[i]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                j = j+1
        return nums