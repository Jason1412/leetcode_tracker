# Last updated: 5/16/2026, 12:26:27 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.valToIndex = {}

        for i in range(len(postorder)):
            self.valToIndex[postorder[i]] = i

        root = self.build(preorder, 0, len(preorder)-1, postorder,
            0, len(postorder)-1)

        return root


    def build(self, preorder, preStart, preEnd, postorder, postStart, 
        postEnd):

        if preStart > preEnd:
            return 
        
        if preStart == preEnd:
            return TreeNode(preorder[preStart])

        rootval = preorder[preStart]

        rootleftval = preorder[preStart+1]

        ind = self.valToIndex[rootleftval]

        leftsize = ind - postStart + 1


        root = TreeNode(rootval)

        root.left = self.build(preorder, preStart+1, preStart+leftsize,
            postorder, postStart, ind)
        root.right = self.build(preorder, preStart+leftsize+1, preEnd,
            postorder, ind+1, postEnd-1)

        return root