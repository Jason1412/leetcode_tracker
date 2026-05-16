# Last updated: 5/16/2026, 12:29:02 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        self.res = []

        self.dfs(root, 1)

        return self.res

    def dfs(self, root, depth):

        if not root:
            return

        if depth > len(self.res):
            self.res.append(root.val)

        self.dfs(root.right, depth+1)
        self.dfs(root.left, depth+1)







    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     if root is None:
    #         return

    #     queue = deque([root])
    #     res = []

    #     while queue:
    #         for i in range(len(queue)):
    #             q = queue.popleft()
    #             if i == 0:
    #                 res.append(q.val)
    #             if q.right:
    #                 queue.append(q.right)
    #             if q.left:
    #                 queue.append(q.left)

    #     return res






















# Method 2 DFS =====================================================
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     self.res = []
    #     depth = 0

    #     self.dfs(root, depth+1)
    #     return self.res

    # def dfs(self, root, depth):

    #     if root is None:
    #         return

    #     if depth > len(self.res):
    #         self.res.append(root.val)


    #     self.dfs(root.right, depth+1)
    #     self.dfs(root.left, depth+1)



# Method 1 BFS =====================================================
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
    #     if not root:
    #         return []

    #     queue = []

    #     queue.append(root)

    #     res = []

    #     while len(queue) > 0:
    #         for i in range(len(queue)):
    #             node = queue.pop(0)

    #             # print("node val=", node.val)
    #             if i == 0:
    #                 res.append(node.val)
            
    #             if node.right:
    #                 queue.append(node.right)
    #             if node.left:
    #                 queue.append(node.left)

    #     return res