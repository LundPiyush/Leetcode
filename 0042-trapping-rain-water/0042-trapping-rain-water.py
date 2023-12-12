class Solution:
    def trap(self, height: List[int]) -> int:
        # OPTIMAL APPROACH ----------> TC- > O(N) SC-> O(1)
        n = len(height)
        res = 0
        left_max,right_max=0,0
        l,r=0,n-1
        
        while l<=r:
            if height[l] <= height[r]:
                if height[l]>=left_max:
                    left_max= height[l]
                else:
                    res = res + (left_max-height[l])
                l = l + 1
            else:
                if height[r]>=right_max:
                    right_max= height[r]
                else:
                    res = res + (right_max-height[r])
                r = r - 1
        return res
                    
        
        
        
        
        
        
        # BETTER APPROACH : ------> TC- > O(3N) SC-> O(2N)
        '''
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
        '''
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