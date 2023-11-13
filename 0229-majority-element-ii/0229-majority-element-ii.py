class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        elements = Counter(nums)
        
        ans =[]
        n = len(nums)
        
        for key,value in elements.items():
            if value > n //3:
                ans.append(key)
        return ans