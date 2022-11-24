
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
        prev=[0]*n
        
        '''
        for space optimazation => dp[i] = cur and dp[i-1] = prev
        '''
        for i in range(0,m):
            cur=[0]*n
            for j in range(0,n):
                if i== 0 and j ==0:
                    cur[j] = grid[i][j]
                else:
                    up,left = float('inf'),float('inf')
                    if i>0:
                        up= grid[i][j] + prev[j]
                    if j>0:
                        left= grid[i][j] + cur[j-1]
                    cur[j] = min(up,left)
            prev = cur                    
        return prev[n-1]
        #return self.f(m-1,n-1,grid,dp) -> recursion