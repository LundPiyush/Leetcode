
class Solution:
    def f(self,i,j,a,dp):
        if i== 0 and j ==0:
            return a[i][j]
        if i<0 or j<0:
            return float('inf')
        if dp[i][j]!=-1:
            return dp[i][j]
        up= a[i][j] + self.f(i-1,j,a,dp)
        left= a[i][j] + self.f(i,j-1,a,dp)
        dp[i][j] = min(up,left)
        return dp[i][j]
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        return self.f(m-1,n-1,grid,dp)