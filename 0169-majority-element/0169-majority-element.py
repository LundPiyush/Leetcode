class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        storing ele,count in hash_map and iterating over hash_map
        TC => O(Nlogn) + O(n) 
        SC =>O(x) 
        x = unique elements 
        
        hash_map={}
        for ele in nums:
            if ele not in hash_map:
                hash_map[ele]=1
            else:
                hash_map[ele]= hash_map[ele] + 1
        n = len(nums)
        for key,element in hash_map.items():
            if element > n // 2:
                return key
        '''
        
        '''
        Moore Voting algorithm
        TC=> O(n) + O(n)
        SC => O(1)
        '''
        
        cnt = 0
        ele = None
        n= len(nums)
        for i in range(n):
            if cnt == 0:
                ele = nums[i]
                cnt+=1
            elif ele == nums[i]:
                cnt+=1
            else:
                cnt-=1
        #verifying step 
        cnt2=0
        for i in range(n):
            if ele == nums[i]:
                cnt2+=1
        if cnt2 >n//2:
            return ele
        