class Solution:
    def f(self,i,j,arr,dp):
        if arr[i][j] == 1:
            return 0
        if i == 0 and j ==0:
            return 1
        if i<0 or j<0:
            return 0
        
        if dp[i][j]!=-1:
            return dp[i][j]
        left = self.f(i,j-1,arr,dp)
        up = self.f(i-1,j,arr,dp)
        dp[i][j] = left + up
        return dp[i][j]
        
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]*n for _ in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j==0:
                    dp[i][j] = 1
                else:
                    left , up = 0,0
                    if j>0:
                        left = dp[i][j-1]
                    if i>0:
                        up = dp[i-1][j]
                    dp[i][j] = left + up
        return dp[m-1][n-1]
        #return self.f(m-1,n-1,obstacleGrid,dp)