# Last updated: 5/16/2026, 12:25:58 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_gap = 0

        self.getMinMax(root)

        return self.max_gap

    def getMinMax(self, root):

        if root is None:
            return sys.maxsize, - sys.maxsize

        left_min, left_max = self.getMinMax(root.left)
        right_min, right_max = self.getMinMax(root.right)

        self.max_gap = max(self.max_gap, root.val - min(left_min, right_min), max(left_max, right_max) - root.val)

        out_min = min(left_min, right_min, root.val)
        out_max = max(left_max, right_max, root.val)

        return out_min, out_max