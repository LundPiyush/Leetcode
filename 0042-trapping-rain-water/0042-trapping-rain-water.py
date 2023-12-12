class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        prefix_sum = [0]*n
        sufix_sum = [0]*n
        prefix_sum[0] = height[0]
        
        for i in range(1,n):
            prefix_sum[i] = max(prefix_sum[i-1],height[i])
            
        sufix_sum[n-1]= height[n-1]
        
        for i in range(n-2,-1,-1):
            sufix_sum[i] = max(sufix_sum[i+1],height[i])
        
        for i in range(n):
            res+= min(prefix_sum[i],sufix_sum[i])- height[i]
        
        return res
    
        # Bute force TC - > O(N^2)
        '''
        n = len(height)
        res=0
        for i in range(n):
            left,right=0,0
            j = i
            while j >=0:
                left = max(left,height[j])
                j = j-1
            j = i
            while j <n:
                right = max(right,height[j])
                j = j+1
            res += min(left,right) - height[i] 
        return res            
        '''