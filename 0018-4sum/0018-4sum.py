class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
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