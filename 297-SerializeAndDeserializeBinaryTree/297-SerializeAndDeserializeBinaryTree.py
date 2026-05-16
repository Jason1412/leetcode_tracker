# Last updated: 5/16/2026, 12:28:35 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
SEP = ","
NULL = "#"

from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        
        queue = deque([root])
        se_list = []

        while queue:
            q = queue.popleft()
            if q is None:
                se_list.append(NULL)
                continue
            
            se_list.append(str(q.val))

            queue.append(q.left)
            queue.append(q.right)

        return ",".join(se_list)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = data.split(',')

        root_val = int(nodes[0])

        root = TreeNode(root_val)
        queue = deque([root])

        # print("nodes=", nodes)

        i = 1
        while i <= len(nodes)-1:
            # print(queue)

            parent = queue.popleft()

            left = nodes[i]

            # print("left=", left)
            if left != NULL:
                parent.left = TreeNode(int(nodes[i]))
                queue.append(parent.left)
                # print("parent=", parent)
            else:
                parent.left = None
            i += 1

            right = nodes[i]
            if right != NULL:
                parent.right = TreeNode(int(nodes[i]))
                queue.append(parent.right)

            else:
                parent.right = None
            i += 1

        # print("root=", root)

        return root

            
            
            

            


        





# Method 1: pre-order ====================================================
    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     tree_list = []
    #     self.se_dfs(root, tree_list)
    #     return SEP.join(tree_list)


    # def se_dfs(self, root, tree_list):
        
    #     if root is None:
    #         tree_list.append(NULL)
    #         return
        
    #     tree_list.append(str(root.val))


    #     self.se_dfs(root.left, tree_list)
    #     self.se_dfs(root.right, tree_list)


        

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     tree_list = data.split(",")
        
    #     root = self.de_dfs(tree_list)
    #     return root
    


    # def de_dfs(self, tree_list):

    #     if not tree_list:
    #         return None

    #     first = tree_list.pop(0)
    #     if first == NULL:
    #         return None
        
    #     root = TreeNode(first)

    #     root.left = self.de_dfs(tree_list)
    #     root.right = self.de_dfs(tree_list)
        
    #     return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))