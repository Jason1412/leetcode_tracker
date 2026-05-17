# Last updated: 5/16/2026, 9:14:42 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def flatten(self, root: Optional[TreeNode]) -> None:
9        """
10        Do not return anything, modify root in-place instead.
11        """
12        
13        if root is None:
14            return
15
16        self.flatten(root.left)
17        self.flatten(root.right)
18
19        left = root.left
20        right = root.right
21
22        root.left = None
23        root.right = left
24
25        p = root
26        while p.right:
27            p = p.right
28        
29        p.right = right
30
31