class Solution:
    def lengthOfLongestSubstring(self, a: str) -> int:
        if len(a) == 0:
            return 0
        n = len(a)
        st = set()
        maxi = 0
        left, right =0,0
        while right < n:
            if a[right] in st:
                while a[right] in st and left<= right:
                    st.remove(a[left])
                    left +=1
            st.add(a[right])
            maxi = max(maxi,right-left+1)
            right+=1
        return maxi
            
        
       
            