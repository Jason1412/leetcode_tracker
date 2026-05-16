# Last updated: 5/16/2026, 12:26:35 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque, defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.graph = defaultdict(list)

        self.build(root, None)

        self.out = []
        self.visited = set()
        self.dfs(target, 0, k)
        return self.out


    def build(self, root, parent):
        if root and parent:
            self.graph[root].append(parent)
            self.graph[parent].append(root)

        if root.left:
            self.build(root.left, root)
        if root.right:
            self.build(root.right, root)

    def dfs(self, root, distance, k):
        if root is None or root in self.visited:
            return

        if distance == k:
            self.out.append(root.val)

        self.visited.add(root)

        for neighbor in self.graph[root]:
            self.dfs(neighbor, distance+1, k)
        

        





# Method 1 =============================================================
# parent pointer
# from collections import deque
# class Solution:
#     def __init__(self):
#         self.parent = {}

#     def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
#         self.traverse(root, None)

#         queue = deque([target])
#         out = []
#         steps = 0
#         visited = set()
#         visited.add(target)

#         while queue:
            
#             for i in range(len(queue)):
#                 q = queue.popleft()
#                 visited.add(q)

#                 if steps == k:
#                     out.append(q.val)

#                 if self.parent.get(q, 0) and self.parent[q] not in visited:
#                     queue.append(self.parent[q])
#                     visited.add(self.parent[q])
#                 if q.left and q.left not in visited:
#                     queue.append(q.left)
#                     visited.add(q.left)
#                 if q.right and q.right not in visited:
#                     queue.append(q.right)
#                     visited.add(q.right)

#             steps += 1

#             # if steps == k:
#             #     return [node.val for node in queue]

#         return out

        
#     def traverse(self, root, parent):

#         if root is None:
#             return

#         self.parent[root] = parent

#         self.traverse(root.left, root)
#         self.traverse(root.right, root)


    
        