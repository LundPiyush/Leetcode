class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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