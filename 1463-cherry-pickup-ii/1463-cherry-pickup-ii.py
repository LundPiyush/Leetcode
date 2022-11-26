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
        
        # explore all paths for alice and bob SIMULTANEOUSLY
        for d1 in range(-1,2,1): # d1 goes from  -1 -> 1
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
        
        '''
        Tabulation
        1. Base case : a. reaching destination => n -1  
        2. Express i,j1,j2 in terms of for loops and copy recurence
        3. Return max
        '''
        
        # Base case 
        
        for j1 in range(0,m):
            for j2 in range(0,m):
                if j1==j2:
                    dp[n-1][j1][j2] = grid[n-1][j1]
                else:
                    dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
                
        # explore all paths for alice and bob SIMULTANEOUSLY

        for i in range(n-2,-1,-1):
            for j1 in range(0,m):
                for j2 in range(0,m):
                    maxi=float('-inf')
                    for d1 in range(-1,2,1): # d1 goes from  -1 -> 1
                        for d2 in range(-1,2,1):
                            value = 0
                            if j1 == j2:
                                if j1+d1>=0 and j2+d2>=0 and j1+d1<m and j2+d2<m:
                                    value = max(value,grid[i][j1] + dp[i+1][j1+d1][j2+d2])      
                                else:
                                    value+=float('-inf')
                            else:
                                if j1+d1>=0 and j2+d2>=0 and j1+d1<m and j2+d2<m:
                                    value = max(value,grid[i][j1] + grid[i][j2] + dp[i+1][j1+d1][j2+d2])
                                else:
                                    value+=float('-inf')
                            maxi = max(maxi,value)
                    dp[i][j1][j2] = maxi
        return dp[0][0][m-1]
        
        
        
        
        
        #return self.f(0,0,m-1,n,m,grid,dp) => recursion 