# Last updated: 5/16/2026, 12:25:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        res = []

        while queue:

            layer_sum = 0
            for i in range(len(queue)):
                q = queue.popleft()

                layer_sum += q.val

                if q.left:
                    queue.append(q.left)

                if q.right:
                    queue.append(q.right)

            res.append(layer_sum)

        return res[-1]       