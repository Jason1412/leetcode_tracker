# Last updated: 5/17/2026, 7:55:07 PM
# Traverse method
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        
10        self.depth = 0
11        self.res = []
12
13        self.traverse(root)
14
15        return self.res
16
17
18    def traverse(self, root):
19
20        if root is None:
21            return
22
23
24        self.depth += 1
25        if self.depth > len(self.res):
26            self.res.append(root.val)
27        
28        
29        self.traverse(root.right)
30        self.traverse(root.left)
31
32        self.depth -= 1