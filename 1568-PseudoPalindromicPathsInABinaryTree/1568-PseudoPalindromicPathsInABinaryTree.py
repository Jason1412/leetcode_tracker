# Last updated: 5/16/2026, 12:25:33 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:

# Method 2 =============================================================
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = [0 for _ in range(10)]
        self.res = 0

        self.dfs(root)

        return self.res


    def dfs(self, root):
        
        if root is None:
            return

        self.count[root.val] += 1

        if not root.left and not root.right:

            tmp = 0
            for freq in self.count:
                if freq % 2 == 1:
                    tmp += 1
                
            if tmp <= 1:
                self.res += 1
        
        self.dfs(root.left)
        self.dfs(root.right)

        self.count[root.val] -= 1
                    


    


# Method 1 =============================================================
    # def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
    #     self.path = []
    #     self.res = 0

    #     self.dfs(root)

    #     return self.res

        
    # def dfs(self, root):

    #     if root is None:
    #         return


    #     self.path.append(root.val)

    #     if not root.left and not root.right:
    #         if self.checkPalin(self.path):
    #             self.res += 1

    #     self.dfs(root.left)
    #     self.dfs(root.right)

    #     self.path.pop()
        

    # def checkPalin(self, input_list):
    #     # At most one element has appeared odd time.
    #     count_dict = Counter(input_list)
        
    #     count = 0

    #     for key, val in count_dict.items():
    #         if val % 2 == 1:
    #             count += 1

    #         if count >= 2:
    #             return False

    #     return True
