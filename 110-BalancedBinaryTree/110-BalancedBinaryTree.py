# Last updated: 5/16/2026, 12:29:51 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True

        self.findHeight(root)

        return self.flag

    def findHeight(self, root):

        if root is None:
            return 0

        leftHeight = self.findHeight(root.left)
        rightHeight = self.findHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            self.flag = False

        return max(leftHeight, rightHeight) + 1