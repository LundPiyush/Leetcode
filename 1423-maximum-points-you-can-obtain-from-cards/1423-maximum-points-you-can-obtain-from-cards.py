class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum,rsum =0,0
        n = len(cardPoints)

        #calculating first k elements sum from front 
        for i in range(k):
            lsum= lsum + cardPoints[i]

        max_sum = lsum

        rIndex = n-1
        # removing one element from front and adding same element to the back
        for i in range(k-1,-1,-1):
            lsum = lsum - cardPoints[i]
            rsum = rsum + cardPoints[rIndex]
            rIndex -= 1
            max_sum = max(max_sum, lsum+rsum)
            
        return max_sum
