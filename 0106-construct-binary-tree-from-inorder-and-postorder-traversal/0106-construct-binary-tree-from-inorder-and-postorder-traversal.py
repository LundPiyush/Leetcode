# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,postorder,postStart,postEnd,inorder,inStart,inEnd,map):
        if postStart > postEnd or inStart > inEnd:
            return None
        root = TreeNode(postorder[postEnd])
        inRoot = map[root.val]
        numsLeft = inRoot - inStart

        root.left  = self.helper(postorder,postStart,postStart+numsLeft-1,inorder,inStart,inRoot-1,map)
        root.right = self.helper(postorder,postStart +numsLeft,postEnd-1,inorder,inRoot+1,inEnd,map)
        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)!=len(postorder):
            return None
        map ={}
        for i in range(len(inorder)):
            map[inorder[i]] =i
        root=self.helper(postorder,0,len(postorder)-1,inorder,0,len(inorder)-1,map)
        return root
        