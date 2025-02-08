# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [(root,1)]

        while queue:
            node,depth = queue.pop(0)

            # if leaf node, return depth
            if not node.left and not node.right:
                return depth

            # traverse and push into queue
            if node.left:
                queue.append((node.left,depth + 1))
            if node.right:
                queue.append((node.right,depth + 1))

            