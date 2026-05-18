# Last updated: 5/18/2026, 11:38:36 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8from collections import deque
9class Solution:
10    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
11        
12        if not root:
13            return 0
14
15        q = deque([(root, 1)])
16
17        maxWidth = 0
18
19
20
21        while q:
22            sz = len(q)
23
24
25            minLevel = 3001
26            maxLevel = -1
27
28            for i in range(sz):
29                node, index = q.popleft()
30                # minLevel = min(index, minLevel)
31                # maxLevel = max(index, maxLevel)
32
33                if i == 0:
34                    start = index
35
36                if i == sz - 1:
37                    end = index
38                # print("minLevel=", minLevel)
39                # print("maxLevel=", maxLevel)
40                # print("----------")
41
42                if node.left:
43                    q.append((node.left, index * 2))
44                
45                if node.right:
46                    q.append((node.right, index * 2 + 1))
47
48        
49            maxWidth = max(end - start + 1, maxWidth)
50
51
52        return maxWidth