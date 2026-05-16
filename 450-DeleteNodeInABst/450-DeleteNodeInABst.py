# Last updated: 5/16/2026, 12:27:56 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        

        if root is None:
            return None

        if root.val == key:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            

            minNode = self.getminNode(root.right)

            minNode.right = self.deleteNode(root.right, minNode.val)
            minNode.left = root.left
            root = minNode

        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        return root

    def getminNode(self, root):
        while root.left:
            root = root.left
        return root