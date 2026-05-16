# Last updated: 5/16/2026, 12:25:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Method 2 ============================================
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0
        self.dfs(root, root.val)

        return self.count

    def dfs(self, root, pathMax):
        if root is None:
            return 

        if root.val >= pathMax:
            self.count += 1
            pathMax = root.val

        self.dfs(root.left, pathMax)
        self.dfs(root.right, pathMax)




# Method 1 ============================================
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         self.count = 1

#         self.onPath = []

#         self.dfs(root)

#         return self.count

#     def dfs(self, root):
#         if root is None:
#             return

#         if len(self.onPath) > 0:
#             if root.val >= max(self.onPath):
#                 self.count += 1

#         self.onPath.append(root.val)

#         self.dfs(root.left)
#         self.dfs(root.right)

#         self.onPath.pop()
        
