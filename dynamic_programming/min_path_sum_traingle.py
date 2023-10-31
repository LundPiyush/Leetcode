'''Probelem - 
https://www.codingninjas.com/codestudio/problems/triangle_1229398

Note: start point(0,0) - fixed , end point - variable => (n,0)...(n,n)
'''
def f(i,j,a,n,dp):
    if i==n-1:
        return a[n-1][j]
    if dp[i][j]!=-1:
        return dp[i][j]
    down = a[i][j] + f(i+1,j,a,n,dp)
    diagonal = a[i][j] + f(i+1,j+1,a,n,dp)
    dp[i][j] = min(down,diagonal)
    return dp[i][j]
        
def minimumPathSum(triangle, n):
    # Write your code here.
    dp=[[-1]*n for _ in range(n)]
    
    # to fill last row of dp(n*n) same as last row a(n*n)
    for j in range(0,n):
        dp[n-1][j] = triangle[n-1][j]
    
    for i in range(n-2,-1,-1):
        for j in range(i,-1,-1):
            down = triangle[i][j] + dp[i+1][j]
            diagonal = triangle[i][j] + dp[i+1][j+1]
            dp[i][j] = min(down,diagonal)
    return dp[0][0]
    #return f(0,0,triangle,n,dp) - > recursion solution 