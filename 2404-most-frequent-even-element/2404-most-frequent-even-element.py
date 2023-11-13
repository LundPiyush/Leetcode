class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq_map= {}
        n = len(nums)
        
        for i in range(n):
            if nums[i]%2 ==0:
                if nums[i] in freq_map:
                    freq_map[nums[i]]+=1
                else:
                    freq_map[nums[i]] = 1
        output =-1
        max_count=0
        
        for ele,count in freq_map.items():
            if count > max_count:
                max_count = count
                output = ele
            elif count == max_count:
                output = min(ele,output)
        return output
            
        
        
        
            
        
        