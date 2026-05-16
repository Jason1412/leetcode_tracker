# Last updated: 5/16/2026, 12:25:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])

        level = 0
        while queue:
            
            prev, cur = None, None

            for i in range(len(queue)):
                q = queue.popleft()
                
                if i == 0:
                    prev = q.val
                elif i == 1:
                    cur = q.val
                else:
                    prev = cur
                    cur = q.val

                if not self.check_valid(level, prev, cur):
                    return False

                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)

            level += 1
        return True

    def check_valid(self, level, prev, cur):
        if level % 2 == 0:
            if prev:
                if prev % 2 == 0:
                    return False
        
            if cur:
                if cur % 2 == 0:
                    return False

            if prev and cur:
                if cur <= prev:
                    return False

        if level % 2 == 1:
            if prev:
                if prev % 2 == 1:
                    return False
            
            if cur:
                if cur % 2 == 1:
                    return False

            if prev and cur:
                if cur >= prev:
                    return False
                
        return True
