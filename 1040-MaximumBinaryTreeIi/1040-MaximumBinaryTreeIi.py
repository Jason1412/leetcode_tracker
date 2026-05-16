# Last updated: 5/16/2026, 12:26:04 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if val > root.val:
            tmp = TreeNode(val)
            tmp.left = root
            return tmp
        
        self.insert(root, val)
        return root



    def insert(self, root, val):

        if val < root.val:
            if root.right is None:
                root.right = TreeNode(val)
            elif root.right.val < val:
                tmp = TreeNode(val)
                tmp.left = root.right
                root.right = tmp
            else:
                self.insert(root.right, val)

        
