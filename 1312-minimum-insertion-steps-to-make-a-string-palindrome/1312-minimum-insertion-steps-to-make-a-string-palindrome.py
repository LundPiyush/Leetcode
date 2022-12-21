class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        
        Logic is reverse the string given(s1) and store in s2
        now find lcs(s1,s2)=> Longest common subsequence for s1 and s2 
        lcs found from s1 and s2 will be pallindromic as s2 is reverse of s1
        
        '''
        str1 = s
        n = len(str1)
        str2 = "".join(reversed(str1))
        
        dp=[[0]*(n+1) for _ in range(n+1)]
    
        for ind1 in range(1,n+1):
            for ind2 in range(1,n+1):
                if str1[ind1-1] == str2[ind2-1]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                
                else:
                    dp[ind1][ind2] = max(dp[ind1-1][ind2],dp[ind1][ind2-1])
        return dp[n][n]
    def minInsertions(self, s: str) -> int:
        n = len(s)
        return n - self.longestPalindromeSubseq(s)