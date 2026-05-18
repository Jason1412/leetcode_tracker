# Last updated: 5/17/2026, 7:26:17 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumNumbers(self, root: Optional[TreeNode]) -> int:
9        self.res = 0
10        self.path = 0
11
12        self.traverse(root)
13        return self.res
14
15    def traverse(self, root):
16
17        if root is None:
18            return
19
20
21        self.path = self.path * 10 + root.val
22
23        if root.left is None and root.right is None:
24            self.res += self.path
25            self.path = self.path // 10
26            return 
27
28        self.traverse(root.left)
29        self.traverse(root.right)
30        
31        self.path = self.path // 10