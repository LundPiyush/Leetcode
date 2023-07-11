class Solution:
    def reverse (self, nums, i, j) : 
        li = i
        ri = j
        
        while li < ri:
            temp = nums[li]
            nums[li] = nums[ri]
            nums[ri] = temp
            
            li += 1
            ri -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k% n
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-1)
        
        
    
    