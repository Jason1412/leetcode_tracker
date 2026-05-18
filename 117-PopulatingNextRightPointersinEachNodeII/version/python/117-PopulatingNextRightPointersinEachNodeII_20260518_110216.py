# Last updated: 5/18/2026, 11:02:16 AM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
5        self.val = val
6        self.left = left
7        self.right = right
8        self.next = next
9"""
10from collections import deque
11
12class Solution:
13    def connect(self, root: 'Node') -> 'Node':
14        
15
16        if not root:
17            return None
18
19        
20        q = deque([root])
21
22        while q:
23            sz = len(q)
24
25            prevNode = None
26
27            for i in range(sz):
28
29                node = q.popleft()
30
31                node.next = prevNode
32                prevNode = node
33
34                if node.right:
35                    q.append(node.right)
36
37                if node.left:
38                    q.append(node.left)
39
40        return root
41
42        