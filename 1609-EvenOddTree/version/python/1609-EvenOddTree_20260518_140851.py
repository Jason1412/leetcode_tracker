# Last updated: 5/18/2026, 2:08:51 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
10        
11        q = deque([root])
12
13        depth = 0
14
15        while q:
16            sz = len(q)
17            prevNode = None
18            for i in range(sz):
19                node = q.popleft()
20
21                if prevNode is not None:
22                    
23                    if depth % 2 == 0:
24                        if node.val <= prevNode.val:
25                            return False
26
27                    if depth % 2 == 1:
28                        if node.val >= prevNode.val:
29                            return False
30
31                if depth % 2 == 0:
32                    if node.val % 2 == 0:
33                        return False
34                if depth % 2 == 1:
35                    if node.val % 2 == 1:
36                        return False
37
38
39
40                prevNode = node
41
42                if node.left:
43                    q.append(node.left)
44
45                if node.right:
46                    q.append(node.right)
47
48            depth += 1
49        return True
50
51
52