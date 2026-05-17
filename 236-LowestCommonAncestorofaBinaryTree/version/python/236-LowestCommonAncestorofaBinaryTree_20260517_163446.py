# Last updated: 5/17/2026, 4:34:46 PM
# Check root at post-order position.
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        
11        lca = self.find(root, p, q)
12
13        if lca is not None:
14            return lca
15        return None
16
17
18
19    def find(self, root, p, q):
20
21        if root is None:
22            return
23
24
25
26        left = self.find(root.left, p, q)
27        right = self.find(root.right, p, q)
28
29
30        if root == p or root == q:
31            return root
32
33
34        if left is not None and right is not None:
35            return root
36
37        
38        if left is None:
39            return right
40        else:
41            return left
42
43