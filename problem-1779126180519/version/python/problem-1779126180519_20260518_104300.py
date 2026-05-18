# Last updated: 5/18/2026, 10:43:00 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
10        
11        if not root:
12            return []
13
14        depth = 0
15        q = deque([root])
16        res = []
17        level = []
18
19        while q:
20            sz = len(q)
21            
22            for i in range(sz):
23                node = q.popleft()
24
25                level.append(node.val)
26
27                if node.left:
28                    q.append(node.left)
29                if node.right:
30                    q.append(node.right)
31            
32            if depth % 2 == 1:
33                level.reverse()
34            
35            res.append(level)
36            level = []
37            depth += 1
38
39        return res
40