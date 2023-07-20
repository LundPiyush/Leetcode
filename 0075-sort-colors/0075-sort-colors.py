class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        using Dutch national flag algorithm
        TC=>O(N)
        SC=>O(1)
        
        approach 2:
        
        take 3 counts(count1,count2,count3) and iterate over array and store the counts and run 3 loops
        1. 0       -  count1  => store 0
        2. count+1 -  count2  => store 1
        3. count2+1 - count3  => store 2
        and modify the original array
        
        '''
        
        n = len(nums)
        low = 0 
        mid = 0
        high = n-1
        
        while(mid<=high):
            if nums[mid]==0:
                nums[mid],nums[low] = nums[low],nums[mid]
                low+=1
                mid+=1
            
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1
        return nums
        