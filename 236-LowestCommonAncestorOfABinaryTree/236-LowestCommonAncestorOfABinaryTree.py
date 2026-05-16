# Last updated: 5/16/2026, 12:28:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        return self.dfs(root, p, q)
    
    def dfs(self, root, p, q):


        if root is None:
            return

        if root == p or root == q:
            return root


        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)


        
        if left and right:
            return root
        
        if left and not right:
            return left

        if right and not left:
            return right

        
        

























# # Method 1 ==========================================================
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

#         depth = 0
#         return self.find(root, p, q, depth)
        

#     def find(self, root, p, q, depth):
#         if root is None:
#             return 
        
#         depth += 1

#         left = self.find(root.left, p, q, depth)
#         right = self.find(root.right, p, q, depth)

#         if root == p or root == q:
#             return root

#         if left is not None and right is not None:
#             print(depth * ">>>" + "root=", root.val)
#             return root

#         if left is None and right is not None:
#             print(depth * ">>>" + "right=", right.val)
#             return right

#         if right is None and left is not None:
#             print(depth * ">>>" + "left=", left.val)
#             return left