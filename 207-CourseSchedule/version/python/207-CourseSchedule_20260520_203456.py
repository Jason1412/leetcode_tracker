# Last updated: 5/20/2026, 8:34:56 PM
# BFS
1from collections import deque
2class Solution:
3    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
4        # DFS ======================================================        
5        # graph = self.buildGraph(numCourses, prerequisites)
6
7        # self.onPath = [False] * numCourses
8        # self.hasCycle = False
9        # self.visited = [False] * numCourses
10
11        # for i in range(numCourses):
12        #     self.visited.append(i)
13        #     self.dfs(graph, i)
14
15        # return not self.hasCycle
16        # DFS Ends ==================================================
17
18        # BFS
19
20        graph = self.buildGraph(numCourses, prerequisites)
21
22        indegree = [0] * numCourses
23
24        for edge in prerequisites:
25            from_, to_ = edge[1], edge[0]
26            indegree[to_] += 1
27                
28        q = deque([])
29
30        for i in range(numCourses):
31            if indegree[i] == 0:
32                q.append(i)
33
34        count = 0
35
36        while q:
37            sz = len(q)
38
39            for i in range(sz):
40                index = q.popleft()
41                count += 1
42
43                for next_ in graph[index]:
44
45                    indegree[next_] -= 1
46
47                    if indegree[next_] == 0:
48                        q.append(next_)
49        
50        return count == numCourses
51
52
53    def buildGraph(self, numCourses, prerequisites):
54
55
56        graph = [[] for _ in range(numCourses)]
57
58        for edge in prerequisites:
59            from_, to_ = edge[1], edge[0]
60            graph[from_].append(to_)
61
62        return graph
63
64    # def dfs(self, graph, i):
65
66    #     if self.onPath[i]:
67    #         self.hasCycle = True
68    #         return
69
70    #     if self.hasCycle:
71    #         return
72
73    #     if self.visited[i]:
74    #         return
75
76
77    #     self.onPath[i] = True
78    #     self.visited[i] = True
79
80    #     for neighbor in graph[i]:
81    #         self.dfs(graph, neighbor)
82        
83    #     self.onPath[i] = False
84