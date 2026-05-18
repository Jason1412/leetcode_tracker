# Last updated: 5/18/2026, 1:45:51 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
10        
11        if not root:
12            return 
13
14        q = deque([root])
15
16        res = 0
17        maxVal = float('-inf')
18        depth = 0
19
20        while q:
21            sz = len(q)
22            depth += 1
23            levelSum = 0
24            
25            for i in range(sz):
26                node = q.popleft()
27                levelSum += node.val
28                
29                if node.left:
30                    q.append(node.left)
31
32                if node.right:
33                    q.append(node.right)
34
35
36            if levelSum > maxVal:
37                maxVal = levelSum
38                res = depth
39
40
41        return res
42                
43            
44
45        
46