# Last updated: 5/16/2026, 12:29:54 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        self.val2ind = {}

        for i in range(len(inorder)):
            self.val2ind[inorder[i]] = i
    
        root = self.build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
        
        return root


    def build(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if inStart > inEnd:
            return

        if inStart == inEnd:
            return TreeNode(inorder[inStart])

        root_val = postorder[postEnd]

        ind = self.val2ind[root_val]

        root = TreeNode(root_val)

        leftsize = ind - inStart
        

        root.left = self.build(inorder, inStart, ind-1, postorder, 
            postStart, postStart+leftsize-1)

        root.right = self.build(inorder, ind+1, inEnd, postorder,
            postStart+leftsize, postEnd-1)

        return root
