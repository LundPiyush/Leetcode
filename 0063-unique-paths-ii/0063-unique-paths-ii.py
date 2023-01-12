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
        return self.f(m-1,n-1,obstacleGrid,dp)