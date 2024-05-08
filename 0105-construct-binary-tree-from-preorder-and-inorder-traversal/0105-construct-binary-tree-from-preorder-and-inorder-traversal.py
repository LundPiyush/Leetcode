# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,preorder,preStart,preEnd,inorder,inStart,inEnd,map):
        if preStart > preEnd or inStart > inEnd:
            return None
        root = TreeNode(preorder[preStart])
        inRoot = map[root.val]
        numsLeft = inRoot - inStart

        root.left  = self.helper(preorder,preStart + 1,preStart+numsLeft,inorder,inStart,inRoot-1,map)
        root.right = self.helper(preorder,preStart+numsLeft+1,preEnd,inorder,inRoot+1,inEnd,map)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map ={}
        for i in range(len(inorder)):
            map[inorder[i]] =i
        root=self.helper(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,map)
        return root
