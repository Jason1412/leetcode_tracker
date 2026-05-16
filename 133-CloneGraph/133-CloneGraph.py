# Last updated: 5/16/2026, 12:29:30 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import collections
from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None:
            return

        nodes = self.cloneNodes(node)

        mappings = self.createMappings(nodes)

        self.cloneEdges(nodes, mappings)
        return mappings[node]


    def cloneNodes(self, node):
        queue = deque([node])
        visited = set([node])

        while queue:
            q = queue.popleft()

            for neighbor in q.neighbors:
                if neighbor and neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return list(visited)


    def createMappings(self, list_nodes):
        mappings = {}
        for node in list_nodes:
            mappings[node] = Node(node.val)
        return mappings


    def cloneEdges(self, list_nodes, mappings):

        for node in list_nodes:
            for neighbor in node.neighbors:
                if neighbor:
                    mappings[node].neighbors.append(mappings[neighbor])










# Method 2 ===================================================
    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

    #     if not node:
    #         return None
        
    #     nodes = self.cloneNodes(node)
    #     mappings = self.createMappings(nodes)
    #     self.cloneEdges(nodes, mappings)

    #     return mappings[node]
        

    # def cloneNodes(self, node):
    #     queue = deque()
    #     visited = set()

    #     queue.append(node)
    #     visited.add(node)

    #     while queue:
    #         q = queue.popleft()

    #         if q.neighbors:
    #             for neighbor in q.neighbors:

    #                 if neighbor in visited:
    #                     continue

    #                 queue.append(neighbor)
    #                 visited.add(neighbor)
        
    #     return list(visited)


    # def createMappings(self, nodes):
    #     mappings = {}
    #     for node in nodes:
    #         mappings[node] = Node(node.val)
    #     return mappings


    # def cloneEdges(self, nodes, mappings):

    #     for node in nodes:
    #         if node.neighbors:
    #             for neighbor in node.neighbors:
    #                 mappings[node].neighbors.append(mappings[neighbor])







    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
    #     # Steps:
    #     # 1. Find all the nodes
    #     # 2. Find the mappings between old nodes and new nodes
    #     # 3. Find all the neighbors of a given node
        

    #     if node is None:
    #         return None


    #     # if not node:
    #     #     return None

    #     nodes = self.findNodes(node)

    #     mappings = self.buildMappings(nodes)

    #     cloneEdges = self.cloneEdges(mappings)

    #     return mappings[node]
        

    # def findNodes(self, node):

    #     queue = collections.deque([node])
    #     visited = {node}

    #     while queue:
    #         q = queue.popleft()
    #         if q.neighbors is not None:
    #             for neighbor in q.neighbors:
    #                 if neighbor not in visited:
    #                     visited.add(neighbor)
    #                     queue.append(neighbor)

    #     return list(visited)


    # def buildMappings(self, nodes):
    #     # nodes: List
        
    #     mappings = {}
    #     for node in nodes:
    #         mappings[node] = Node(node.val)

    #     return mappings


    # def cloneEdges(self, mappings):

    #     for old_node, new_node in mappings.items():
    #         if old_node.neighbors is not None:
    #             for neighbor in old_node.neighbors:
    #                 new_node.neighbors.append(mappings[neighbor])
        

        


    

        