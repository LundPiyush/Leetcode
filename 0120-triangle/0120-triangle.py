class Solution:
    def f(self,i,j,a,n,dp):
        if i == n-1:
            return a[i][j]
        if dp[i][j] != 0:
            return dp[i][j]
        down = a[i][j] + self.f(i+1,j,a,n,dp)
        daigonal = a[i][j] + self.f(i+1,j+1,a,n,dp)
        dp[i][j] = min(down,daigonal)
        return dp[i][j]
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n= len(triangle)
        dp=[[0]*n for _ in range(n)]
        
        # filling last row
        for j in range(0,n):
            dp[n-1][j] = triangle[n-1][j]
        
        # i starts from second last row as we have already filled last row
        # j starts from i and ends at 0 as for every i there are i+1 elements
        # ^ for i=2 -> j=0,1,2 (3 elements)
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                down = triangle[i][j] + dp[i+1][j]
                daigonal = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down,daigonal)
        return dp[0][0]
        #return self.f(0,0,triangle,n,dp) => recursion