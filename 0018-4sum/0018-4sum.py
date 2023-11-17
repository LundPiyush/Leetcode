class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # TWO POINTER APPROACH
        # TC -> O(N3)   SC-> O(no. of quadruplets) This space is only used to store the answer.
        
        ans =[]
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i>0 and nums[i]== nums[i-1]:
                continue
            for j in range(i+1,n):
                if j!=i+1 and nums[j]== nums[j-1]:
                    continue
                k,l = j+1, n-1
                while k<l:
                    if nums[i]+ nums[j]+ nums[k]+ nums[l] < target:
                        k = k+1
                    elif nums[i]+ nums[j]+ nums[k]+ nums[l] > target:
                        l = l-1
                    else:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k = k+1
                        l = l-1
                        while k<l and nums[k]==nums[k-1]:
                            k = k+1
                        while k<l and nums[l]==nums[l+1]:
                            l = l-1
        return ans
        '''
        Better approach 
        TC -> O(N3*log(M)), where N = size of the array, M = no. of elements in the set.
        SC=> O(2 * no. of the quadruplets)+O(N)
        
        ans = []
        st = set()
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1,n):
                hashset=set()
                for k in range(j+1,n):
                    fourth = target - (nums[i]+nums[j]+nums[k])
                    if fourth in hashset:
                        temp=[nums[i],nums[j],nums[k],fourth]
                        temp.sort()
                        st.add(tuple(temp))
                    hashset.add(nums[k])
        return list(st)
        '''