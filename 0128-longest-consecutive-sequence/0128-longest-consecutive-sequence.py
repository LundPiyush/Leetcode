class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ''' Time Complexity: O(N) + O(2*N) ~ O(3*N), where N = size of the array.
            Reason: O(N) for putting all the elements into the set
                    After that for every starting element, we are finding the consecutive elements. Though                       we are using nested loops, the set will be traversed at most twice in the worst case. So, the time complexity is O(2*N) instead of O(N2).

Space Complexity: O(N), as we are using the set data structure to solve this problem.
'''
        n = len(nums)
        st= set()
        if n ==0:
            return 0
        # adding elements in the set
        for ele in nums:
            st.add(ele)
        longest=1
        for ele in st:
            if ele - 1 not in st: # this means ele is Starting point of the sequence
                cnt = 1
                x = ele
                # find consecutive numbers
                while x+1 in st:
                    x= x+1
                    cnt+=1
                longest=max(longest,cnt)
        return longest

    '''
    # Better approach
     TC- O(NlogN) + O(N)
     SC- O(1)
        lastSmaller = float('-inf')
        currCount = 0
        longest = 1
        n = len(nums)
        if n == 0:
            return 0
        nums.sort()
        for i in range(n):
            if lastSmaller == nums[i]-1:
                currCount +=1
                lastSmaller = nums[i]
            elif nums[i]!= lastSmaller:
                currCount =1
                lastSmaller = nums[i]
            longest = max(longest,currCount)
        return longest
        
    ''' 
        
        
    '''
    def linearSearch(self,a,num):
        n = len(a)
        
        for i in range(n):
            if a[i] == num:
                return True
        return False
    
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==0:
            return 0
        longest = 1
        for i in range(n):
            x= nums[i]
            cnt = 1
            while self.linearSearch(nums,x+1):
                x+=1
                cnt+=1
            longest = max(longest,cnt)
        return longest
    '''