# Last updated: 5/16/2026, 12:26:07 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        queue = deque([(0, 0, root)])
        rec = defaultdict(list)


        while queue:

            for i in range(len(queue)):
                row, col, node = queue.popleft()

                rec[col].append((row, node.val))

                if node.left:
                    queue.append((row+1, col-1, node.left))

                if node.right:
                    queue.append((row+1, col+1, node.right))

        sorted_keys = list(rec.keys())

        sorted_keys.sort()

        out = []
        for key in sorted_keys:
            out.append(item[1] for item in sorted(rec[key]))

        return out