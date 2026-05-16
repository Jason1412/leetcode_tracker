# Last updated: 5/16/2026, 12:28:48 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.out = 0
        self.rank = 0
        
        self.traverse(root, k)

        return self.out

    
    def traverse(self, root, k):
        if root is None:
            return
        
        if self.rank == k:
            return

        self.traverse(root.left, k)

        self.rank += 1
        self.out = root.val
        
        self.traverse(root.right, k)
  




# # Method 3 ========================================================= 
#     class KthSmallestFound(Exception):
#         pass

#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         self.rank = 0
#         self.out = 0
#         try:
#             self.traverse(root, k)
#         except self.KthSmallestFound:
#             return self.out

#     def traverse(self, root, k):
#         if root is None:
#             return
        
#         self.traverse(root.left, k)

#         self.rank += 1
#         if self.rank == k:
#             self.out = root.val
#             raise self.KthSmallestFound()  # Raise an exception to break out of all recursion
        
#         self.traverse(root.right, k)


    # Method 2 ======================================================

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
    #     self.rank = 0
    #     self.out = 0

    #     self.traverse(root, k)

    #     return self.out


    # def traverse(self, root, k):
    #     if root is None:
    #         return

    #     self.traverse(root.left, k)

    #     self.rank += 1
        
    #     if self.rank == k:
    #         self.out = root.val
    #         return 

    #     self.traverse(root.right, k)




    # Method 1 ======================================================
    # Iteration method 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []

        while root:
            stack.append(root)
            root = root.left
        

        for _ in range(k-1):
            
            root = stack.pop()

            if root.right:
                root = root.right

                while root:
                    stack.append(root)
                    root = root.left

        return stack[-1].val 