'''
Problem - https://www.codingninjas.com/codestudio/problems/ninja-s-training_3621003
'''

def f(day,last,points,dp):
    if day == 0:
        maxi = 0
        for i in range(0,3):
            if i!=last:
                maxi=max(maxi,points[0][i])
        return maxi
    if dp[day][last]!=-1:
        return dp[day][last]
    maxi = 0
    for i in range(0,3):
        if i!=last:
            point = points[day][i] + f(day-1,i,points,dp)
            maxi= max(maxi,point)
    dp[day][last] = maxi
    return dp[day][last]
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    dp = [ [0]*4 for _ in range(n)]
    
    # Base condtion for day = 0
    dp[0][0] = max(points[0][1],points[0][2])
    dp[0][1] = max(points[0][0],points[0][2])
    dp[0][2] = max(points[0][0],points[0][1])
    dp[0][3] = max(points[0][0],points[0][1],points[0][2])

    for day in range(1,n):
        for last in range(0,4):
            maxi = 0
            for i in range(0,3):
                if i!=last:
                    point = points[day][i] + dp[day-1][i]
                    maxi= max(maxi,point)
            dp[day][last] = maxi
    return dp[n-1][3] 
    
    #return f(n-1,3,points,dp)  // for recursion solution we call function f defined at the start

'''
Time complexity - O(N*3*4) => O(N)
Space complexity - O(N*4)
'''