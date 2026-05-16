# Last updated: 5/16/2026, 12:26:16 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import sys
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque()
        flag = 0

        queue.append(root)

        while queue:
            q = queue.popleft()

            if q is None and flag == 0:
                flag = 1
            
            if flag == 1 and q is not None:
                return False

            if q:
                queue.append(q.left)
                queue.append(q.right)
        
        return True


























    # def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        

    #     queue = deque([root])

    #     flag = False

    #     while queue:
            
    #         for i in range(len(queue)):
    #             q = queue.popleft()

    #             if q is None:
    #                 flag = True
    #             else:
    #                 if flag:
    #                     return False

    #                 queue.append(q.left)
    #                 queue.append(q.right)
                
    #     return True
        