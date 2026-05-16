# Last updated: 5/16/2026, 12:29:33 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root):
        self.cumSum = 0
        self.pathSum = 0

        self.dfs(root, 0)
        return self.cumSum

    def dfs(self, root, prev):
        if root is None:
            return 

        pathSum = prev * 10 + root.val

        if root.left is None and root.right is None:
            self.cumSum += pathSum

        self.dfs(root.left, pathSum)
        self.dfs(root.right, pathSum)
# Method 3 ==============================================
# Divide and Conquer
    # def sumNumbers(self, root):

    #     return self.dfs(root, 0)    
    

    # def dfs(self, root, prev):
        
    #     if root is None: # 存在一些node只有left subtree or right subtree的情况
    #         return 0

    #     cumSum = prev * 10 + root.val
    #     if root.left is None and root.right is None:
    #         return cumSum

    #     leftSum = self.dfs(root.left, cumSum)
    #     rightSum = self.dfs(root.right, cumSum)

    #     return leftSum + rightSum
        

# Method 2 ==============================================
    # def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
    #     self.path = ''
    #     self.res = 0

    #     self.dfs(root)

    #     return self.res

    # def dfs(self, root):
    #     if not root:
    #         return None

    #     self.path += str(root.val)
    #     if not root.left and not root.right:
    #         self.res += int(self.path)

    #     self.dfs(root.left)
    #     self.dfs(root.right)

    #     self.path = self.path[:-1]  # pop the last element in string


# Method 1 ==============================================
    # def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
    #     self.res = []
    #     self.track = []

    #     self.dfs(root)

    #     print(self.res)

    #     out = 0
    #     for item in self.res:
    #         num = 0
    #         for digit in item:
    #             num = 10 * num + digit
    #         out += num
    #     return out


    # def dfs(self, root):
    #     if not root:
    #         return


    #     self.track.append(root.val)
    #     if root.left is None and root.right is None:
    #         self.res.append(self.track.copy())

    #     self.dfs(root.left)
    #     self.dfs(root.right)
 
    #     self.track.pop()



