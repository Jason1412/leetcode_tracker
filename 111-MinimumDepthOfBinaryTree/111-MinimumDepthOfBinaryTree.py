# Last updated: 5/16/2026, 12:29:50 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
    
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):

                q = queue.popleft()
                
                if q.left is None and q.right is None:
                    return depth

                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)


