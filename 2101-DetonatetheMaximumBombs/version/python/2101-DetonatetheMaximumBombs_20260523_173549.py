# Last updated: 5/23/2026, 5:35:49 PM
1from collections import deque
2class Solution:
3    def maximumDetonation(self, bombs: List[List[int]]) -> int:
4        
5        graph = self.buildGraph(bombs)
6        
7
8        max_count = 0
9        for i in range(len(bombs)):
10            count = self.bfs(graph, i)
11            max_count = max(max_count, count)
12
13        return max_count
14
15
16
17    def buildGraph(self, bombs):
18        n = len(bombs)
19        graph = [[] for _ in range(n)]
20
21        for i in range(n):
22            for j in range(n):
23                if i == j:
24                    continue
25
26                if self.isConnected(bombs[i], bombs[j]):
27                    graph[i].append(j)
28
29        return graph
30    
31
32    def isConnected(self, bomb1, bomb2):
33        distSquare = (bomb1[0] - bomb2[0]) ** 2 + (bomb1[1] - bomb2[1]) ** 2
34
35        return (bomb1[2]) ** 2 >= distSquare
36
37        
38    def bfs(self, graph, src):
39        visited = [False] * len(graph)
40        q = deque([src])
41        visited[src] = True
42        count = 0
43
44        while q:
45            node = q.popleft()
46            count += 1
47            for neighbor in graph[node]:
48
49                if visited[neighbor]:
50                    continue
51
52                q.append(neighbor)
53                visited[neighbor] = True
54                
55        return count
56