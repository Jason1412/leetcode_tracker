# Last updated: 5/16/2026, 12:29:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        return self.flatten_return_last_node(root)


    def flatten_return_last_node(self, root):
        if root is None:
            return None

        left_last = self.flatten_return_last_node(root.left)
        right_last = self.flatten_return_last_node(root.right)

        
        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        if left_last and right_last:
            return right_last

        if right_last is None and left_last:
            return left_last

        if left_last is None and right_last:
            return right_last

        if left_last is None and right_last is None:
            return root

