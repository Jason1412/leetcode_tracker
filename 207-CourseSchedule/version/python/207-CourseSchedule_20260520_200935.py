# Last updated: 5/20/2026, 8:09:35 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        
4        graph = self.buildGraph(numCourses, prerequisites)
5
6        self.onPath = [False] * numCourses
7        self.hasCycle = False
8        self.visited = [False] * numCourses
9
10        for i in range(numCourses):
11            self.visited.append(i)
12            self.dfs(graph, i)
13
14        return not self.hasCycle
15
16
17    def buildGraph(self, numCourses, prerequisites):
18
19
20        graph = [[] for _ in range(numCourses)]
21
22        for edge in prerequisites:
23            from_, to_ = edge[1], edge[0]
24            graph[from_].append(to_)
25
26        return graph
27
28    def dfs(self, graph, i):
29
30        if self.onPath[i]:
31            self.hasCycle = True
32            return
33
34        if self.hasCycle:
35            return
36
37        if self.visited[i]:
38            return
39
40
41        self.onPath[i] = True
42        self.visited[i] = True
43
44        for neighbor in graph[i]:
45            self.dfs(graph, neighbor)
46        
47        self.onPath[i] = False
48