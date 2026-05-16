# Last updated: 5/16/2026, 12:27:08 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0

        self.maxLen(root)

        return self.res


    def maxLen(self, root):

        if root is None:
            return 0

        left = self.maxLen(root.left)
        right = self.maxLen(root.right)

        l, r = 0, 0
        if root.left and root.left.val == root.val:
            l = left + 1
        
        if root.right and root.right.val == root.val:
            r = right + 1

        self.res = max(self.res, l + r)

        return max(l, r)