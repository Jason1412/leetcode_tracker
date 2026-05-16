# Last updated: 5/16/2026, 12:29:59 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = []
        res = []

        queue.append(root)
       
        while queue:
            res.append([node.val for node in queue])
            for i in range(len(queue)):
                q = queue.pop(0)

                if q and q.left:
                    queue.append(q.left)
                if q and q.right:
                    queue.append(q.right)

            
        
        return res
