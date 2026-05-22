# Last updated: 5/21/2026, 8:23:56 PM
1import heapq
2
3class State:
4    def __init__(self, node, distFromStart):
5        self.node = node
6        self.distFromStart = distFromStart
7
8    def __lt__(self, other):
9        return self.distFromStart < other.distFromStart
10
11
12class Solution:
13    def buildgraph(self, times, n):
14        graph = [[] for _ in range(n+1)]
15        for edge in times:
16            source = edge[0]
17            target = edge[1]
18            weight = edge[2]
19
20            graph[source].append([target, weight])
21
22        return graph
23    
24
25    def dijkstra(self, graph, src):
26        
27        minDistTo = [float('inf') for _ in range(len(graph))]
28
29        pq = []
30
31        heapq.heappush(pq, State(src, 0))
32        minDistTo[src] = 0
33
34        while pq:
35            curState = heapq.heappop(pq)
36            curNode = curState.node
37            curDistFromStart = curState.distFromStart
38
39            if curDistFromStart > minDistTo[curNode]:
40                continue
41
42            for nextState in graph[curNode]:
43                
44                nextNode = nextState[0]
45                weight = nextState[1]
46                nextDistFromStart = curDistFromStart + weight
47
48                if nextDistFromStart >= minDistTo[nextNode]:
49                    continue
50
51                heapq.heappush(pq, State(nextNode, nextDistFromStart))
52                minDistTo[nextNode] = nextDistFromStart
53
54        return minDistTo
55
56    
57    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
58        
59        graph = self.buildgraph(times, n)
60
61        minDistTo = self.dijkstra(graph, k)
62
63        maxDist = 0
64        for i in range(1, n+1):
65            if minDistTo[i] == float('inf'):
66                return -1
67            maxDist = max(maxDist, minDistTo[i])
68
69        return maxDist
70
71
72
73
74
75