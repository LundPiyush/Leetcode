class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n 
        if n == 2:
            return 1
        prev3,prev2,prev = 0,1,1
        curi = 0
        for i in range(3,n+1):
            curi= prev + prev2 + prev3
            prev3 = prev2
            prev2 = prev
            prev = curi
        return prev