class Solution:
    def f(self,i,j1,j2,n,m,a,dp):
        
        #Base case -> Out of bound
        if j1<0 or j2<0 or j1>=m or j2>=m:
            return float('-inf')
        
        #Base case -> destination
        if i==n-1:
            if j1==j2:
                return a[i][j1]
            else:
                return a[i][j1]+a[i][j2]
        if dp[i][j1][j2]!=-1:
            return dp[i][j1][j2]
        maxi = 0 
        for d1 in range(-1,2,1):
            for d2 in range(-1,2,1):
                if j1 == j2:
                    maxi = max(maxi,a[i][j1] + self.f(i+1,j1+d1,j2+d2,n,m,a,dp))
                else:
                    maxi = max(maxi,a[i][j1] + a[i][j2] + self.f(i+1,j1+d1,j2+d2,n,m,a,dp))
        dp[i][j1][j2] = maxi
        return dp[i][j1][j2]
        
        
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp=[[[-1]*m for _ in range(m)]for _ in range(n)]
        return self.f(0,0,m-1,n,m,grid,dp)