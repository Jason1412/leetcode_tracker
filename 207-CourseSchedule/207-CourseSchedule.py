# Last updated: 5/16/2026, 12:28:58 PM
from collections import deque
class Solution:
# Self version 2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses, prerequisites)
        visited = [False for _ in range(numCourses)]
        onPath = set()

        self.flag = True

        for i in range(numCourses):
            if not self.flag:
                return False
            self.dfs(i, visited, graph, onPath)

        return self.flag


    def dfs(self, i, visited, graph, onPath):
        if i in onPath:
            self.flag = False
            return

        if not self.flag or visited[i]:
            return

        if graph[i] is None:
            return



        onPath.add(i)
        visited[i] = True
        for neighbor in graph[i]:
            self.dfs(neighbor, visited, graph, onPath)
        onPath.remove(i)


    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            src, tgt = edge[1], edge[0]
            graph[src].append(tgt)

        return graph























# Self version 1:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

    #     # Steps:
    #     # 1. Find the indegrees of each node.
    #     # 2. Put the nodes with indegree = 0 into the queue.
    #     # 3. BFS 

    #     graph, indegree = self.buildGraph(numCourses, prerequisites)

    #     queue = deque()
    #     count = 0

    #     for i in range(len(indegree)):
    #         if indegree[i] == 0:
    #             queue.append(i)
    #             count += 1
        
    #     while queue:

    #         q = queue.popleft()
            
    #         for node in graph[q]:
    #             indegree[node] -= 1
    #             if indegree[node] == 0:
    #                 queue.append(node)
    #                 count += 1

    #     return count == numCourses
            

    # def buildGraph(self, numCourses, prerequisites):
    #     graph = [[] for _ in range(numCourses)]
    #     indegree = [0 for _ in range(numCourses)]

    #     for edge in prerequisites:
    #         graph[edge[1]].append(edge[0])
    #         indegree[edge[1]] += 1
        
    #     return graph, indegree

    


# Method 2 BFS =========================================================
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    

    # # Step 1: Build the graph, find indegree of each node
    # # Step 2: BFS on each starting node. Only traverse on nodes with
    # # indegree = 0
    # # Step 3: check if the number of traversed nodes = total number of nodes
    #     self.indegree = [0 for _ in range(numCourses)]
    #     graph = self.buildGraph(numCourses, prerequisites)
    #     count = 0
    #     print("graph=", graph)
    #     print("indegree=", self.indegree)

    #     queue = []

    #     for i in range(numCourses):
    #         if self.indegree[i] == 0:
    #             count += 1 
    #             queue.append(i)

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
    #         # for i in range(numCourses): # This will keep taking the previous node into account. 
    #         #     if self.indegree[i] == 0:
    #         #         count += 1
    #         #         queue.append(i)

    #     return count == numCourses
        

    # def buildGraph(self, numCourses, prerequisites):
    #     graph = [[] for _ in range(numCourses)]
        
    #     for edge in prerequisites:
    #         src = edge[1]
    #         target = edge[0]
    #         self.indegree[target] += 1
    #         graph[src].append(target)

    #     return graph




# Method 1 DFS =========================================================
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
    # # Step 1: Build the graph
    # # Step 2: DFS on each node
    # # Step 3: Check if there is a closed loop
    #     graph = self.buildGraph(numCourses, prerequisites)

    #     self.visited = [False for _ in range(numCourses)]
    #     self.hasCycle = False
    #     self.onPath = [False for _ in range(numCourses)]


    #     self.cycle_node = -1
    #     self.cycle_path = []


    #     for src_node in range(len(graph)):
    #         self.dfs(graph, src_node)

    #     print("cycle node=", self.cycle_node)
    #     print("cycle_path=", self.cycle_path)

    #     return not self.hasCycle


    # def dfs(self, graph, src_node):

    #     if self.onPath[src_node] is True:
    #         self.cycle_node = src_node
    #         self.cycle_path = [i for i in range(len(self.onPath)) if self.onPath[i] is True]

    #         self.hasCycle = True
    #         return

    #     if self.visited[src_node] is True:
    #         return

    #     self.visited[src_node] = True
    #     self.onPath[src_node] = True

    #     for node in graph[src_node]:
    #         self.dfs(graph, node)

    #     self.onPath[src_node] = False







    # def buildGraph(self, numCourses, prerequisites):
    #     graph = [[] for _ in range(numCourses)]

    #     for edge in prerequisites:
    #         source = edge[1]
    #         target = edge[0]
    #         graph[source].append(target)

    #     return graph        
