# Last updated: 5/16/2026, 12:28:57 PM
from collections import deque
class Solution:


# Method 1 BFS v2 ======================================================
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0] * numCourses
        topo_order = []
        graph = [[] for _ in range(numCourses)]

        for node_to, node_from in prerequisites:
            indegree[node_to] += 1
            graph[node_from].append(node_to)


        queue = deque()
        count = 0

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        
        while queue:
            cur_pos = queue.popleft()
            count += 1
            topo_order.append(cur_pos)

            for neighbor in graph[cur_pos]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        
        if count == numCourses:
            return topo_order
        else:
            return []

# Method 1 BFS ==========================================================
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    

    # # Step 1: Build the graph, find indegree of each node
    # # Step 2: BFS on each starting node. Only traverse on nodes with
    # # indegree = 0
    # # Step 3: check if the number of traversed nodes = total number of nodes
    #     self.indegree = [0 for _ in range(numCourses)]
    #     self.res = []
    #     graph = self.buildGraph(numCourses, prerequisites)
    #     count = 0
    #     # print("graph=", graph)
    #     # print("indegree=", self.indegree)

    #     queue = []

    #     for i in range(numCourses):
    #         if self.indegree[i] == 0:
    #             count += 1 
    #             queue.append(i)
    #             self.res.append(i)

    #     while (len(queue) > 0):
    #         n_node = len(queue)
    #         for i in range(n_node):
    #             node = queue.pop(0)

    #             if len(graph[node]) == 0:
    #                 continue

    #             for neibor_node in graph[node]:
    #                 # print("neibor_node=", neibor_node)
    #                 self.indegree[neibor_node] -= 1
    #                 if self.indegree[neibor_node] == 0:
    #                     queue.append(neibor_node)
    #                     count += 1
    #                     self.res.append(neibor_node)
    #         # for i in range(numCourses): # This will keep taking the previous node into account. 
    #         #     if self.indegree[i] == 0:
    #         #         count += 1
    #         #         queue.append(i)

    #     print("traversed nodes=", self.res)


    #     if count == numCourses:
    #         return self.res
    #     else:
    #         return []
        

    # def buildGraph(self, numCourses, prerequisites):
    #     graph = [[] for _ in range(numCourses)]
        
    #     for edge in prerequisites:
    #         src = edge[1]
    #         target = edge[0]
    #         self.indegree[target] += 1
    #         graph[src].append(target)

    #     return graph

    




# Method 2 DFS =========================================================
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

    # # Steps:
    # # 1. Build the graph based on pre-req
    # # 2. Check if has cycle
    # # 3. If no cycle, post-order traverse and reverse the output list.
        
    #     if len(prerequisites) == 0:
    #         return [i for i in range(numCourses)]
        
    #     graph = self.buildGraph(numCourses, prerequisites)
    #     print("graph=", graph)

    #     self.visited = [False for _ in range(numCourses)]
    #     self.onPath = [False for _ in range(numCourses)]
    #     self.hascycle = False
    #     self.postorder = []

    #     self.hasCycle(graph)
    #     print("has cycle=", self.hascycle)
    #     print("postorder=", self.postorder)

    #     if self.hascycle:
    #         return []
    #     else:
    #         self.postorder.reverse()
    #         return self.postorder


    # def buildGraph(self, numCourses, prerequisites):
    #     graph = [[] for _ in range(numCourses)]
        
    #     for edge in prerequisites:
    #         src = edge[1]
    #         target = edge[0]
    #         graph[src].append(target)

    #     return graph


    # def hasCycle(self, graph):
        
    #     for i in range(len(graph)):
    #         # if len(graph[i]) == 0: 
    #         #     continue

    #         self.dfs(i, graph)

    #     return self.hascycle


    # def dfs(self, node, graph):

    #     if self.onPath[node] is True:
    #         self.hascycle = True

    #     if self.visited[node] or self.hascycle:
    #         return 

    #     self.visited[node] = True
    #     self.onPath[node] = True
    #     for neibor_node in graph[node]:
    #         self.dfs(neibor_node, graph)
            
    #     self.postorder.append(node)
    #     self.onPath[node] = False

    

