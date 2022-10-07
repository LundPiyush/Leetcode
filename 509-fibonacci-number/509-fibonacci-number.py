class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n;
        prev2 = 0
        prev = 1
        curi = 0
        for i in range(2,n+1):
            curi = prev + prev2
            prev2 = prev
            prev = curi
            
        return prev