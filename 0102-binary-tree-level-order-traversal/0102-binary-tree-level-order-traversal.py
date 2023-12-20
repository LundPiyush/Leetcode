# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #while there are nodes in the queue, iterate through the number of nodes in the queue (this is the number of nodes in the next level)
        #pop queue(0), add queue(0).val to current level list and append queue(0)'s children to queue
        #append level to ans
        
        ans = []
        queue = []
        if root is None:
            return root 
        
        queue.append(root)
        while len(queue)>0:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)   
            ans.append(level)
        return ans
    
        