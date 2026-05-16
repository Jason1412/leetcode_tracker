# Last updated: 5/16/2026, 12:29:53 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []


        queue = deque([root])
        
        res = deque([])

        while queue:
            layer = []
            for i in range(len(queue)):
                q = queue.popleft()
                layer.append(q.val)
                if q.left:
                    queue.append(q.left)
                
                if q.right:
                    queue.append(q.right)

            res.appendleft(layer)
        return res



# Method 1 =======================================================
    # def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

    #     if not root:
    #         return []


    #     queue = deque([root])
        
    #     res = deque([])

    #     while queue:
    #         res.appendleft([node.val for node in queue])

    #         for i in range(len(queue)):
    #             q = queue.popleft()

    #             if q.left:
    #                 queue.append(q.left)
                
    #             if q.right:
    #                 queue.append(q.right)


    #     return res


