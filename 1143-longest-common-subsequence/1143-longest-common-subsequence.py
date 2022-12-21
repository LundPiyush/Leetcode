class Solution:
    def f(self,ind1,ind2,dp,s,t):
        if ind1<0 or ind2<0:
            return 0
    
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        #match case
        if s[ind1] == t[ind2]:
            dp[ind1][ind2] = 1 + self.f(ind1-1,ind2-1,dp,s,t)
            return dp[ind1][ind2] 
    
        #not-match case
        dp[ind1][ind2] = 0 + max(self.f(ind1-1,ind2,dp,s,t),self.f(ind1,ind2-1,dp,s,t))
        return dp[ind1][ind2]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m= len(text2)
        dp= [[-1]*m for _ in range(n)]
        return self.f(n-1,m-1,dp,text1,text2)
        