# Last updated: 5/17/2026, 5:48:33 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
9        
10        self.res = []
11        self.path = []
12
13        self.traverse(root)
14        return self.res
15
16    def traverse(self, root):
17
18        if root is None:
19            return
20
21        self.path.append(str(root.val))
22
23        if root.left is None and root.right is None:
24            self.res.append("->".join(self.path))
25            self.path.pop()
26            return
27
28        self.traverse(root.left)
29        self.traverse(root.right)
30        self.path.pop()
31