# Last updated: 5/16/2026, 12:29:44 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

# Method 2: BFS
        if root is None:
            return 

        q = []
        q.append(root)

        while len(q) > 0:
            
            size = len(q)
            print("size=", size)

            for i in range(size):
                node = q.pop(0)

                print("node.val = ", node.val)

                if len(q) > 0 and i < size-1:
                    node.next = q[0]
                
                
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return root

            





# Method 1: traverse
    #     if root is None:
    #         return 

    #     self.traverse(root.left, root.right)
    #     return root


    # def traverse(self, node1, node2):

    #     if node1 is None or node2 is None:
    #         return 

    #     node1.next = node2

    #     self.traverse(node1.left, node1.right)
    #     self.traverse(node1.right, node2.left)
    #     self.traverse(node2.left, node2.right)

    #     return 
