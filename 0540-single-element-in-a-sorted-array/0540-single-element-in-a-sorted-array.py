class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        L, R, mid = 0, len(nums)-1, 0
        while L <= R:
            mid = (L + R) >> 1
            isHalfEven = (mid-L) % 2 == 0
            
            if mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                if isHalfEven: L = mid + 2
                else: R = mid - 1
            elif mid and nums[mid] == nums[mid-1]:
                if isHalfEven: R = mid - 2
                else: L = mid + 1
            else: 
                return nums[mid]
                
                
                
            
            
        