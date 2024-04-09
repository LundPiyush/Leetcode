# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_sum = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.PathSum(root)
        return self.max_sum
        
    def PathSum(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0
        left_sum = max(0,self.PathSum(node.left))
        right_sum = max(0,self.PathSum(node.right))
        
        self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)
        
        return node.val + max(left_sum,right_sum)
        