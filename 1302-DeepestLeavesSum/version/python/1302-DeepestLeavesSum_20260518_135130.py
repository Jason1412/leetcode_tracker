# Last updated: 5/18/2026, 1:51:30 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
10        
11        if not root:
12            return 0
13
14        q = deque([root])
15
16        while q:
17            sz = len(q)
18            
19
20            levelSum = 0
21            for i in range(sz):
22                node = q.popleft()
23                levelSum += node.val
24
25                if node.left:
26                    q.append(node.left)
27
28                if node.right:
29                    q.append(node.right)
30
31        return levelSum