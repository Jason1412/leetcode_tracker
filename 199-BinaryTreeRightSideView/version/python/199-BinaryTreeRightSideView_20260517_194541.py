# Last updated: 5/17/2026, 7:45:41 PM
# BFS method.
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
10        
11        res = []
12        depth = 0
13        q = deque([root])
14
15        if root is None:
16            return res
17
18        while q:
19            sz = len(q)
20            depth += 1
21            last = q[0]
22            res.append(last.val)
23
24            for i in range(sz):
25                
26                node = q.popleft()
27                
28                if node.right:
29                    q.append(node.right)
30
31                if node.left:
32                    q.append(node.left)
33
34        return res