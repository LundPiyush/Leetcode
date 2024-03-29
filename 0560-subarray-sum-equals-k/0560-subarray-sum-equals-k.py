class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mpp = {}
        preSum = 0
        cnt = 0

        mpp[0] = 1 # Setting 0 in the map.
        for i in range(n):
            # add current element to prefix Sum:
            preSum += nums[i]

            # Calculate x-k:
            remove = preSum - k

            # Add the number of subarrays to be removed:
            if remove in mpp:
                cnt += mpp[remove]

            # Update the count of prefix sum in the map.
            if preSum in mpp:
                mpp[preSum] += 1
            else:
                mpp[preSum] = 1

        return cnt
        
        '''
        # Brute force        
        n = len(nums)
        count = 0
        
        for i in range(n):
            sum =0
            for j in range(i,n):
                sum += nums[j]
                if sum == k:
                    count +=1
        return count
        '''