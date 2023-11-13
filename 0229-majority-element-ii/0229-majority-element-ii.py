class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # optimal approach - Extended version of Moore's voting algorithm 
        n = len(nums)
        mini_count = n//3
        cnt1,cnt2=0,0
        ele1, ele2 = None,None
        
        for i in range(n):
            if cnt1==0 and ele2!= nums[i]:
                ele1 = nums[i]
                cnt1+=1
            elif cnt2==0 and ele1!= nums[i]:
                ele2 = nums[i]
                cnt2+=1
            elif nums[i] == ele1:
                cnt1+=1
            elif nums[i] == ele2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
                
        #Verifying step:
        ans = []
        cnt1,cnt2=0,0
        for i in range(n):
            if ele1 == nums[i]:
                cnt1+=1
            if ele2 == nums[i]:
                cnt2+=1
        
        if cnt1 > mini_count:
            ans.append(ele1)
        if cnt2 > mini_count:
            ans.append(ele2)
            
        return ans
        
        # TC - > O(n) + O(n)        SC-> O(1)        
        '''
        Hashing method TC - > O(nlogn) SC->O(n)
        
        from collections import Counter
        elements = Counter(nums)
        
        ans =[]
        n = len(nums)
        for key,value in elements.items():
            if value > n //3:
                ans.append(key)
        return ans
        '''