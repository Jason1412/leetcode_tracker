# Last updated: 5/16/2026, 12:26:50 PM
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        self.color = [False for _ in range(n)]
        self.visited = [False for _ in range(n)]
        self.out = True

        for i in range(n):
            if not self.visited[i]:
                self.bfs(i, graph)

        return self.out

    def bfs(self, src_node, graph):

        q = []

        q.append(src_node)

        while (len(q) > 0):
            node = q.pop(0)
            self.visited[node] = True
            # print("before for loop, node=", node)
            # print("visited =", self.visited)
            # print("color =", self.color)
            for next_node in graph[node]:
                if not self.visited[next_node]:
                    # print("next node=", next_node)
                    self.color[next_node] = not self.color[node]
                    q.append(next_node)
                else:
                    if self.color[node] == self.color[next_node]:
                        self.out = False
                        break
            

            

    


# Method 1 ==========================================================
# DFS
    # def isBipartite(self, graph: List[List[int]]) -> bool:
    #     n = len(graph)

    #     self.color = [False for _ in range(n)]
    #     self.visited = [False for _ in range(n)]
    #     self.out = True

    #     for i in range(n):
    #         if not self.visited[i]:
    #             self.dfs(i, graph)

    #     return self.out


    # def dfs(self, node, graph):
    #     if not self.out:
    #         return

    #     self.visited[node] = True

    #     for next_node in graph[node]:
    #         if not self.visited[next_node]:
    #             self.color[next_node] = not self.color[node]

    #             self.dfs(next_node, graph)
    #         else:
    #             if self.color[next_node] == self.color[node]:
    #                 self.out = False
    #                 return



    