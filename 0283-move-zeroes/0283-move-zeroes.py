class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        j = -1
        for i in range(n):
            if (nums[i] == 0):
                j = i
                break
        if j==-1: 
            return nums
        for i in range(j+1,n,1):
            if nums[i]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
        return nums    
        
        
        
        
        '''
        n= len(nums)
        temp =[]
        for i in range(n):
            if nums[i]!=0:
                temp.append(nums[i])
        
        for i in range(len(temp)):
            nums[i] = temp[i]
        
        for i in range(len(temp),n,1):
            nums[i] = 0
            
        return nums
        
        '''