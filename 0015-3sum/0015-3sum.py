class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            # remove duplicates:
            if i>0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1,n-1
            # moving 2 pointers:
            while j <k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j = j+1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k=k-1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j = j+1
                    k = k-1
                    # remove duplicates:
                    while j < k and nums[j] == nums[j-1]:
                        j = j+1
                    while j < k and nums[k] == nums[k+1]:
                        k = k-1
        return ans 
    
    
    
    
        '''
        ans =[]
        st = set()
        n = len(nums)
        for i in range(n):
            hashset = set()
            for j in range(i+1,n):
                third = -(nums[i]+nums[j])
                if third in hashset:
                    temp =[nums[i],nums[j],third]
                    temp.sort()
                    st.add(tuple(temp))
                hashset.add(nums[j])
        ans = list(st)
        return ans
        '''
        
        '''
        BRUTE FORCE APPROACH: TC -> O(N^3)+ O(NO. OF UNIQUE TRIPPLETS FOR STORING IN SET) SC->O(2* NO. OF UNIQUE TRIPPLETS)
        
        ans =[]
        st = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        #store the tripplet
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        st.add(tuple(temp))
        ans = [list(item) for item in st]
        return ans
                                     
        '''