# Last updated: 5/16/2026, 12:28:54 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        val1 = min(p.val, q.val)
        val2 = max(p.val, q.val)

        self.res1 = -1
        self.res2 = -1

        return self.find(root, val1, val2)



    def find(self, root, val1, val2):
        
        if root is None:
            return 

        if val1 <= root.val and root.val <= val2:
            return root

        if val1 > root.val:
            self.res1 = self.find(root.right, val1, val2)

        if root.val > val2:
            self.res2 = self.find(root.left, val1, val2)

        if self.res1 != -1:
            return self.res1
        if self.res2 != -1:
            return self.res2
