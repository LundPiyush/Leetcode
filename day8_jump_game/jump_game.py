'''
Problem - https://leetcode.com/problems/jump-game/
Solution - https://www.youtube.com/watch?v=EgMPjWliYGY
'''

def canJump(self, nums: List[int]) -> bool:
    last_good_index_position = len(nums)-1  
    for i in range(len(nums)-1,-1,-1):
        if i + nums[i] >= last_good_index_position:
            last_good_index_position = i
    return last_good_index_position==0