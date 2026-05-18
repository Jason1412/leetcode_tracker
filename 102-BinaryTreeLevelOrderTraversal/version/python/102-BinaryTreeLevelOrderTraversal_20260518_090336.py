# Last updated: 5/18/2026, 9:03:36 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
10        
11        if not root:
12            return []
13
14        q = deque([root])
15        depth = 0
16        res = []
17        level_nodes = []
18
19        while q:
20            sz = len(q)
21
22            res.append([node.val for node in q])
23
24            for i in range(sz):
25
26                node = q.popleft()
27                
28
29                if node.left:
30                    q.append(node.left)
31
32                if node.right:
33                    q.append(node.right)
34
35        return res
36            
37            
38                
39
40