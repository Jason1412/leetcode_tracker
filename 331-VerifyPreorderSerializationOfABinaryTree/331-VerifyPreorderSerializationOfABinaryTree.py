# Last updated: 5/16/2026, 12:28:25 PM
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        nodes = list(preorder.split(","))
        return self.deserialize(nodes) and len(nodes) == 0

    def deserialize(self, nodes):
        if not nodes:
            return False

        first = nodes.pop(0)
        if first == '#':
            return True
        
        return self.deserialize(nodes) and self.deserialize(nodes)