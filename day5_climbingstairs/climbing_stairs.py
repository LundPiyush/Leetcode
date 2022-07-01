'''
Problem - https://leetcode.com/problems/climbing-stairs
Solution - https://leetcode.com/problems/climbing-stairs/discuss/1531764/Python-%3ADetail-explanation-(3-solutions-easy-to-difficult)-%3A-Recursion-dictionary-and-DP
Explaination -
    We can't use recursion approach that is f(i) = f(i-1) + f(i-2) as it TimeLimit Exceeded
    We use dynamic approach using the same formula
'''

def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    elif n == 2 :
        return 2
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1]= 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i]= dp[i-1] + dp[i-2]
    return dp[n]