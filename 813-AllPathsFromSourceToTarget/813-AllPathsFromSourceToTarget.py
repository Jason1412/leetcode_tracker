# Last updated: 5/16/2026, 12:26:46 PM
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        self.res = []
        self.traverse(graph, 0, path)
        return self.res


    def traverse(self, graph, s, path):
        n = len(graph) # number of nodes in the graph

        path.append(s)

        if s == n-1:    
            self.res.append(path.copy())
            path.pop()
            return 

        for node in graph[s]:
            self.traverse(graph, node, path)
        
        path.pop()
