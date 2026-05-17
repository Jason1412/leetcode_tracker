# Last updated: 5/16/2026, 8:12:21 PM
# Divide and conquer.
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        
10
11        if root is None:
12            return
13
14        left = self.invertTree(root.left)
15        right = self.invertTree(root.right)
16
17        root.left, root.right = right, left
18
19        return root