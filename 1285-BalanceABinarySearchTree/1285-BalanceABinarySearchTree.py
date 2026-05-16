# Last updated: 5/16/2026, 12:25:44 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorder_nodes = []

        self.inorder(root)

        n = len(self.inorder_nodes)

        root = self.build(self.inorder_nodes, 0, n-1)

        return root


    def build(self, nodes, start, end):

        if start > end:
            return None
        mid = (start + end) // 2

        left = self.build(nodes, start, mid-1)
        right = self.build(nodes, mid+1, end)

        nodes[mid].left = left
        nodes[mid].right = right

        return nodes[mid]
                
    


    def inorder(self, root):

        if root is None:
            return

        self.inorder(root.left)

        self.inorder_nodes.append(root)

        self.inorder(root.right)