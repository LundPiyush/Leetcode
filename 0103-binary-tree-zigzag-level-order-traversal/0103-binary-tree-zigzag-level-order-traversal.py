# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result =[]
        # Queue to perform level order traversal
        queue = []
        if not root:
            return result 
        queue.append(root)
        
        # Flag to determine the direction of traversal (left to right or right to left)
        leftToRight = True
            
        # Continue traversal until the queue is empty
        while len(queue) > 0:
            size = len(queue)
            
            # List to store the values of nodes at the current leve
            row = [0] * size
            for i in range(size):
                # Get the front node from the queue
                node = queue.pop(0)
                
                # Determine the index to insert the node's value based on the traversal direction
                index = i if leftToRight else (size-1-i)
                
                # Insert the node's value at the determined index
                row[index] = node.val
                
                # Enqueue the left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Switch the traversal direction for the next level
            leftToRight = not leftToRight
            # Add the current level's values to the result list
            result.append(row)
            
        return result
            