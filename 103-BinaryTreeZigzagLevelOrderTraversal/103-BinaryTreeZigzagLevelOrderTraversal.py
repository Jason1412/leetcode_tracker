# Last updated: 5/16/2026, 12:29:58 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = {}

        self.preOrder(root, 0)

        
        out = []
        for key in self.res.keys():
            if key % 2 == 1:
                self.res[key].reverse()
            out.append(self.res[key])
        return out
        

    def preOrder(self, root, depth):
        
        if root is None:
            return 

        if depth not in self.res:
            self.res[depth] = [root.val]
        else:
            self.res[depth].append(root.val)

        self.preOrder(root.left, depth + 1)
        self.preOrder(root.right, depth + 1)



# Method 3 ====================================================
    # def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     res = []
        
    #     if not root:
    #         return []

    #     queue = deque([root])
    #     is_reverse = False

    #     while queue:
            
    #         level = deque([])

    #         for i in range(len(queue)):

    #             q = queue.popleft()

    #             if is_reverse:
    #                 level.appendleft(q.val)
    #             else:
    #                 level.append(q.val)    

    #             if q.left:
    #                 queue.append(q.left)
    #             if q.right:
    #                 queue.append(q.right)

    #         res.append(list(level))
    #         is_reverse = not is_reverse
    #     return res



# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []

        
#         queue = [root]
#         isForward = 1
#         res = []

#         while queue:
            
#             res.append([node.val for node in queue[::isForward]])
            
#             for i in range(len(queue)):
#                 q = queue.pop(0)
#                 if q.left:
#                     queue.append(q.left)
#                 if q.right:
#                     queue.append(q.right)

#             isForward *= -1

#         return res

            


# Method 1 =========================================================
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []

#         queue = deque([root])
#         rev_flag = True
#         res = []

#         while queue:
#             res.append([node.val for node in queue])
            
#             tmp_q = deque([])
#             for i in range(len(queue)):
#                 q = queue.pop()
                
                
#                 if rev_flag:
#                     if q and q.right:
#                         tmp_q.append(q.right)
#                     if q and q.left:
#                         tmp_q.append(q.left)
#                 else:
#                     if q and q.left:
#                         tmp_q.append(q.left)
#                     if q and q.right:
#                         tmp_q.append(q.right)
            
#             queue = tmp_q.copy()
#             rev_flag = not rev_flag
#         return res