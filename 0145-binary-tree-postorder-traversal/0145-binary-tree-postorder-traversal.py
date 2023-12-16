# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Iterative approach
        if root is None:
            return 
        ans = []
        stack1,stack2=[],[]
        cur = root
        stack1.append(root)
        
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
                
        while stack2:
            ans.append(stack2.pop().val)
        return ans
    
        
        #Recursive approach
        ans = []
        if not root:
            return ans
        def postOrder(node):
            if node:
                postOrder(node.left)
                postOrder(node.right)
                ans.append(node.val)
        postOrder(root)
        return ans