class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen = 0
        zeros=0
        n = len(nums)
        l,r =0,0

        while r<n:
            if nums[r] ==0:
                zeros+=1
            while zeros > k:
                if nums[l] ==0:
                    zeros=zeros-1
                l=l+1
            if zeros <=k:
                maxlen= max(maxlen,r-l+1)
            r=r+1
        return maxlen

