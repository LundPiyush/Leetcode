class Solution:
    def f(self,i,j,dp):
        if i==0 and j ==0:
            return 1
        if i< 0 or j<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        left = self.f(i,j-1,dp)
        up = self.f(i-1,j,dp)
        dp[i][j]=left + up
        return dp[i][j]
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*n for _ in range(m)]
        '''
            steps to convert recursion to dp :-
                1. Base case
                2. explore all states in for loops 
                3. copy the recurence and write
        '''
        dp [0][0] = 1
    
        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j==0:
                    dp[i][j] = 1
                else:
                    left,up = 0,0
                    if j>0:
                        left = dp[i][j-1]
                    if i>0:
                        up = dp[i-1][j]
                    dp[i][j] = left + up
            
        return dp[m-1][n-1]
        
        #return self.f(m-1,n-1,dp)  // recursion solution => the function is defined above