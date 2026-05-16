# Last updated: 5/16/2026, 12:26:29 PM
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = self.buildGraph(n, dislikes)
        self.color = [False for _ in range(n+1)]
        self.visited = [False for _ in range(n+1)]
        self.out = True


        # print("graph=", graph)
        for i in range(n):
            if len(graph[i]) == 0:
                continue
            else:
                if not self.visited[i]:
                    self.dfs(i, graph)

        return self.out




    def buildGraph(self, n, dislikes):
        graph = [[] for _ in range(n+1)]

        for edge in dislikes:
            w = edge[0]
            v = edge[1]
            graph[v].append(w)
            graph[w].append(v)

        return graph


    def dfs(self, node, graph):


        if self.out is False:
            return

        self.visited[node] = True

        for next_node in graph[node]:
            if not self.visited[next_node]:
                self.color[next_node] = not self.color[node]
                self.dfs(next_node, graph)

            else:
                if self.color[next_node] == self.color[node]:
                    self.out = False # cannot be bipartitioned
                    return
    
