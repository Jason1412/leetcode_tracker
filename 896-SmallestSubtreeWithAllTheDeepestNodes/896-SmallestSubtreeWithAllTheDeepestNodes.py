# Last updated: 5/16/2026, 12:26:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Result:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        res = self.maxDepth(root)
        return res.node


    def maxDepth(self, root):

        if root is None:
            return Result(None, 0)
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left.depth == right.depth:
            return Result(root, left.depth+1)

        if left.depth > right.depth:
            left.depth += 1
            return left
        else:
            right.depth += 1
            return right

        





# My version 1 =========================================
# First find deepest nodes, and 
# from collections import deque
# class Solution:
#     def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
#         nodes = self.find_deep_nodes(root)

#         if len(nodes) == 1:
#             return nodes[0]

#         if len(nodes) == 2:
#             node1, node2 = nodes[0], nodes[1]
#             return self.find_LCA(root, node1, node2)

#         stack = []
#         if len(nodes) > 2:
#             node0 = self.find_LCA(root, nodes[0], nodes[1])
#             stack = [node0]

#             for i in range(2, len(nodes)):
#                 tmp_node = stack.pop()
#                 new_lca = self.find_LCA(root, tmp_node, nodes[i])
#                 stack.append(new_lca)
        
#         return stack[0]


#     def find_deep_nodes(self, root):
        
#         queue = deque([root])

#         depth = 0
#         records = defaultdict(list)

#         while queue:
#             sz = len(queue)
#             for i in range(sz):
#                 q = queue.popleft()
#                 records[depth].append(q)

#                 if q.left:
#                     queue.append(q.left)
                    

#                 if q.right:
#                     queue.append(q.right)
#             depth += 1

#         return records[depth-1]   

#     def find_LCA(self, root, p, q):

#         if root is None:
#             return
        
#         if root == p or root == q:
#             return root

#         left = self.find_LCA(root.left, p, q)
#         right = self.find_LCA(root.right, p, q)

#         if left and right:
#             return root
#         if left:
#             return left
#         if right:
#             return right

