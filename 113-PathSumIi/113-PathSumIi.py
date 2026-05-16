# Last updated: 5/16/2026, 12:29:47 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        if root is None:
            return self.res
        self.traverse(root, targetSum, deque())
        return self.res

    # 遍历二叉树
    def traverse(self, root: Optional[TreeNode], num_sum: int, path: deque) -> None:
        if root is None:
            return

        remain = num_sum - root.val

        if root.left is None and root.right is None:
            if remain == 0:
                # 找到一条路径
                path.append(root.val)
                self.res.append(list(path))
                path.pop()
            return

        # 维护路径列表
        path.append(root.val)
        self.traverse(root.left, remain, path)
        # path.pop()

        # path.append(root.val)
        self.traverse(root.right, remain, path)
        path.pop()    



# Method 1 ==========================================================
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
    #     self.track = []
    #     self.res = []


    #     self.dfs(root, 0, targetSum)
    #     return self.res



    # def dfs(self, root, cumSum, targetSum):

    #     if not root:
    #         return

        
    #     cumSum += root.val
    #     self.track.append(root.val)

    #     if not root.left and not root.right and cumSum == targetSum:
    #         self.res.append(self.track.copy())


    #     self.dfs(root.left, cumSum, targetSum)
    #     self.dfs(root.right, cumSum, targetSum)

    #     cumSum -= root.val
    #     self.track.pop()
