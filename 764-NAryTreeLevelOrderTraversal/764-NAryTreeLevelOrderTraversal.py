# Last updated: 5/16/2026, 12:26:58 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []

        queue = deque()
        queue.append(root)

        res = []

        while queue:
            
            layer = []
            for i in range(len(queue)):
                q = queue.popleft()
                layer.append(q.val)
                for child in q.children:
                    if child:
                        queue.append(child)

            
            res.append(layer)

        return res