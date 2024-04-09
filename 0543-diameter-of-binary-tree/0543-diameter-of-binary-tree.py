# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = 0  
    def findMax(self,node):
        # Base case: If the node is None, return 0 indicating the height of an empty tree
        if node is None:
            return 0
        
        # Recursively calculate the height of left and right subtrees
        lh = self.findMax(node.left)
        rh = self.findMax(node.right)
        
        # Update the maxi (diameter) with the maximum of current maxi(diameter )or sum of left and right heights
        self.maxi = max(self.maxi,lh+rh)
        return 1 + max(lh,rh)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.findMax(root)
        return self.maxi
        
    
        