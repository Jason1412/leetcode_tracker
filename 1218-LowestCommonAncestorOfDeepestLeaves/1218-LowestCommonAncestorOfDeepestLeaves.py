# Last updated: 5/16/2026, 12:25:52 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Result:
    def __init__(self, node: TreeNode, depth):
        self.node = node
        self.depth = depth

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        res = self.maxDepth(root)
        return res.node

    
    def maxDepth(self, root):

        if root is None:
            return Result(None, 0)

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # 这个时候需要从leaf node开始思考这个问题, 然后逐步往上走
        # 当root是LCA时
        if left.depth == right.depth:
            return Result(root, left.depth+1)


        # 当root不是LCA时
        # LCA应该在较大depth的那一侧, 需要把那个LCA一层一层往上传

        if left.depth > right.depth:
            left.depth += 1
            return left
        else:
            right.depth += 1
            return right
        