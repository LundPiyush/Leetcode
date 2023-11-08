class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        
        while True:
            slow = nums[slow]
            slow2= nums[slow2]
            if slow == slow2:
                return slow
    ''' 
        frequency_hash={}
        for i in range(len(nums)):
            if nums[i] in frequency_hash:
                frequency_hash[nums[i]] = frequency_hash[nums[i]] + 1
            else:
                frequency_hash[nums[i]] = 1
          
        for k in frequency_hash.keys():
            if frequency_hash[k]>1:
                return k
    '''        
    '''
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]
    '''
        
        
            