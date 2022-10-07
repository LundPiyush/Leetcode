class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        
        prev2 =1
        prev = 2
        curi = 0
        for i in range(3,n+1):
            curi = prev + prev2
            prev2 = prev
            prev = curi
        return prev