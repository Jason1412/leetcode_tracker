# Last updated: 5/16/2026, 12:26:25 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        
        self.root = root
        self.queue = deque([])
        tmp_q = deque([root])

        while (tmp_q):

            q = tmp_q.popleft()

            if q.left:
                tmp_q.append(q.left)

            if q.right:
                tmp_q.append(q.right)

            if q.left is None or q.right is None:
                self.queue.append(q)    


    def insert(self, val: int) -> int:
        
        q = self.queue[0]
        node = TreeNode(val)

        if q.left is None:
            q.left = node
        elif q.right is None:
            q.right = node
            self.queue.popleft()
        
        self.queue.append(node)

        return q.val





    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()