# Last updated: 5/16/2026, 12:27:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = None

        self.dfs(root, subRoot)
        return self.res

    def dfs(self, root, subRoot):

        if root is None:
            return

        # if self.res is not None:
        #     return
        if self.res is True:
            return

        if root.val == subRoot.val:
            # print(root.val)
            # print(subRoot.val)
            self.res = self.isSameTree(root, subRoot)

        self.dfs(root.left, subRoot)
        self.dfs(root.right, subRoot)

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)