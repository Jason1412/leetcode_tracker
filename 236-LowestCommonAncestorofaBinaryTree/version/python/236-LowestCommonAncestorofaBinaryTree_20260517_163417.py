# Last updated: 5/17/2026, 4:34:17 PM
# Check root at pre-order position.
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
25        if root == p or root == q:
26            return root
27
28
29        left = self.find(root.left, p, q)
30        right = self.find(root.right, p, q)
31
32
33        if left is not None and right is not None:
34            return root
35
36        
37        if left is None:
38            return right
39        else:
40            return left
41
42