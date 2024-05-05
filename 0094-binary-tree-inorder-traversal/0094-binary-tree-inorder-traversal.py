# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        ans =[]

        while cur:
            if cur.left is None:
                ans.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right !=cur:
                    prev = prev.right
                if prev.right is None:
                    prev.right=cur
                    cur = cur.left
                else:
                    prev.right = None
                    ans.append(cur.val)
                    cur = cur.right

        return ans



'''
        # Iterative approach
        cur = root
        ans = []
        stack = []
        while True:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            else:
                if len(stack) == 0:
                    break
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
        return ans

        # Recursive approach
        ans = []
        if not root:
            return ans

        def inOrder(node):
            if node:
                inOrder(node.left)
                ans.append(node.val)
                inOrder(node.right)

        inOrder(root)
        return ans
'''