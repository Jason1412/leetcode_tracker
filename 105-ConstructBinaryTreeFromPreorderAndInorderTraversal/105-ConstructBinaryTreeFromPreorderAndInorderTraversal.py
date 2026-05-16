# Last updated: 5/16/2026, 12:29:56 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.node2index = {}

        for i in range(len(inorder)):
            self.node2index[inorder[i]] = i

        root = self.build(preorder, 0, len(preorder)-1, 
            inorder, 0, len(inorder)-1)
        
        return root


    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        
        if preStart > preEnd:
            return

        rootval = preorder[preStart]
        root = TreeNode(rootval)

        index = self.node2index[rootval]
        leftsize = index - inStart
        
        root.left = self.build(preorder, preStart+1, preStart+leftsize,
        inorder, inStart, index-1)

        root.right = self.build(preorder, preStart+leftsize+1, preEnd,
        inorder, index+1, inEnd)

        return root
