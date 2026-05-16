# Last updated: 5/16/2026, 12:27:18 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        queue = deque([root])
        out = []

        while queue:

            sz = len(queue)
            layer_sum = 0.

            for i in range(sz):
                
                q = queue.popleft()

                layer_sum += q.val

                if q.left:
                    queue.append(q.left)

                if q.right:
                    queue.append(q.right)

            out.append(layer_sum / sz)
        return out
                

