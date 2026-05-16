# Last updated: 5/16/2026, 12:28:29 PM
class Solution:


# Method 2 ==========================================================
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        graph = [set() for _ in range(n)]
        num_nodes = n

        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        leaves = []
        for i, nodes in enumerate(graph):
            if len(nodes) == 1:
                leaves.append(i)
        
        
        while num_nodes > 2:
            num_nodes -= len(leaves)
        
            for i in range(len(leaves)):
                leaf = leaves.pop(0)

                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)


                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
                    
        
        return leaves



# Method 1 ==========================================================
    # def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
    #     if not edges:
    #         return [0]

    #     graph = [[] for _ in range(n)]
    #     num_nodes = n

    #     for edge in edges:
    #         graph[edge[0]].append(edge[1])
    #         graph[edge[1]].append(edge[0])

    #     leaves = []
    #     for i, nodes in enumerate(graph):
    #         if len(nodes) == 1:
    #             leaves.append(i)
        
    #     print(leaves)
        
    #     while num_nodes > 2:
    #         num_nodes -= len(leaves)
        
    #         for i in range(len(leaves)):
    #             leaf = leaves.pop(0)

    #             neighbor = graph[leaf]

    #             graph[neighbor[0]].remove(leaf)

    #             if len(graph[neighbor[0]]) == 1:
    #                 leaves.append(neighbor[0])
                    
        
    #     return leaves


