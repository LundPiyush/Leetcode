'''
Problem - https://leetcode.com/problems/jump-game-ii/
Solution - https://www.youtube.com/watch?v=dJ7sWiOoK7g
'''

def jump(self, nums: List[int]) -> int:
    jumps = 0
    l=r=0
    
    while r < len(nums)-1: # till right ptr reaches last position
        farthest = 0
        for i in range(l,r+1):
            farthest= max(farthest,i+nums[i])
        l=r+1
        r=farthest
        jumps+=1
    return jumps