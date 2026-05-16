# Last updated: 5/16/2026, 12:26:02 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        start = 0
        end = len(preorder) - 1

        root = self.build(preorder, start, end)
        return root



    def build(self, preorder, start, end):
        if start > end:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        p = start + 1

        root = TreeNode(preorder[start])

        while p <= end and preorder[p] < preorder[start]:
            p += 1
        
        root.left = self.build(preorder, start+1, p-1)
        root.right = self.build(preorder, p, end)

        return root

        