class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Brute force -> 
        TC => O(n^2) 
        SC = >  O(1) 
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        return -1
        
        '''
        '''
        Optimal 
        TC => O(n)
        SC =>O(1)
        '''
        n = len(nums)
        s2=0
        for ele in nums:
            s2 = s2+ele 
        sum  = n*(n+1)//2 - s2
        return sum
        
        
        