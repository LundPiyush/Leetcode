'''
Problem - https://leetcode.com/problems/single-number/submissions/
Solution - https://www.youtube.com/watch?v=v6s3l3ezNQI
'''

'''
Explaination -
    Use bitwise XOR
        1. a ^ a = 0
        2. a ^ 0 = a
        3. a ^ b = b ^ a ... Cummulative
    array -> [2,1,4,1,2]
    xor = 2 ^ 1 ^ 4 ^ 1 ^ 2 -> 4 (a ^ a = 0.. 2 and 1 gets canceled)  
'''
def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ nums[i]
        return ans