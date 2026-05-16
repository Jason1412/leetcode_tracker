# Last updated: 5/16/2026, 12:25:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.treesum = 0
        self.res = 0

        self.treesum = self.findSum(root)

        self.findSum(root)

        return int(self.res % (1e9 + 7))


    def findSum(self, root):
        
        if root is None:
            return 0
        
        left = self.findSum(root.left)
        right = self.findSum(root.right)

        sub_sum = left + right + root.val

        self.res = max(self.res, sub_sum * (self.treesum - sub_sum))

        return sub_sum