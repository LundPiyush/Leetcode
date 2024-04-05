# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive approach 
        # Intution -  1 + max(depth of left subtree, depth of right subtree)
        # using post order as we have to calculate left height then right height then add it 1 to current node 
        
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return 1 + max(left,right)