# Last updated: 5/23/2026, 7:54:43 AM
1import heapq
2
3class State:
4    def __init__(self, row, col, minEffort):
5        self.row = row
6        self.col = col
7        self.minEffort = minEffort
8
9    def __lt__(self, other):
10        return self.minEffort < other.minEffort
11    
12
13class Solution:
14
15    def find_neighbors(self, matrix, state):
16        nrow, ncol = len(matrix), len(matrix[0])
17
18        cur_row = state.row
19        cur_col = state.col
20        
21        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
22
23        neighbors = []
24
25        for d in dirs:
26            next_row = cur_row + d[0]
27            next_col = cur_col + d[1]
28            
29            if next_row < 0 or next_col < 0 or next_row > nrow - 1 or next_col > ncol - 1:
30                continue
31
32            neighbors.append([next_row, next_col])
33
34        return neighbors
35
36
37    def dijkstra(self, matrix):
38        nrow, ncol = len(matrix), len(matrix[0])
39
40        distTo = [[float('inf') for _ in range(ncol)] for _ in range(nrow)]
41
42        q = []
43        heappush(q, State(0, 0, 0))
44        distTo[0][0] = 0
45
46        while q:
47            cur_state = heapq.heappop(q)
48            cur_row = cur_state.row
49            cur_col = cur_state.col
50            cur_minEffort = cur_state.minEffort
51
52            if cur_state.minEffort > distTo[cur_row][cur_col]:
53                continue
54
55            if cur_row == nrow - 1 and cur_col == ncol - 1:
56                return distTo[cur_row][cur_col]
57
58
59            for next_ind in self.find_neighbors(matrix, cur_state):
60                
61                next_row = next_ind[0]
62                next_col = next_ind[1]
63
64                next_minEffort = max(cur_minEffort, abs(matrix[next_row][next_col] - matrix[cur_row][cur_col]))
65
66                if next_minEffort >= distTo[next_row][next_col]:
67                    continue
68
69                heapq.heappush(q, State(next_row, next_col, next_minEffort))
70                distTo[next_row][next_col] = next_minEffort
71
72        return -1
73
74
75
76    
77        
78
79    def minimumEffortPath(self, heights: List[List[int]]) -> int:
80        
81
82
83        ans = self.dijkstra(heights)
84
85        return ans
86
87
88    