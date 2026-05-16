# Last updated: 5/16/2026, 12:30:02 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.helper(root, None, None)

    def helper(self, root, min_node, max_node):

        if root is None:
            return True

        if min_node and min_node.val >= root.val:
            return False
        
        if max_node and root.val >= max_node.val:
            return False

        return self.helper(root.left, min_node, root) and \
            self.helper(root.right, root, max_node)