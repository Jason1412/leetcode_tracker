# Last updated: 5/16/2026, 8:09:59 PM
# Post-order traversal
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        
10        self.traverse(root)
11        return root
12
13    
14    def traverse(self, root):
15
16        if root is None:
17            return
18
19        self.traverse(root.left)
20
21        self.traverse(root.right)
22
23        root.left, root.right = root.right, root.left