# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack=[root]
        
        while stack:
            temp = stack.pop()
            if temp:
                ans.append(temp.val)
                if temp.right:
                    stack.append(temp.right) #as we are using stack which works on LIFO, we need to push right tree first so that left will be popped out
                if temp.left:
                    stack.append(temp.left)
        return ans
        
        # TC - O(N), SC - O(N)
        '''
        Recursive approach
        ans = []
        if not root:
            return ans
        def preOrder(node):
            if node:
                ans.append(node.val)
                preOrder(node.left)
                preOrder(node.right)
        preOrder(root)
        return ans
            
        '''