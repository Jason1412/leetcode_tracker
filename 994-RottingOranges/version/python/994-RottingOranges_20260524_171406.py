# Last updated: 5/24/2026, 5:14:06 PM
1from collections import deque
2class Solution:
3    def orangesRotting(self, grid: List[List[int]]) -> int:
4        
5        nrow, ncol = len(grid), len(grid[0])
6
7        q = deque([])
8
9        for i in range(nrow):
10            for j in range(ncol):
11                if grid[i][j] == 2:
12                    q.append((i, j))
13
14        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
15        step = 0
16        while q:
17            sz = len(q)
18            for i in range(sz):
19                row, col = q.popleft()
20
21                for d in dirs:
22                    next_row = row + d[0]
23                    next_col = col + d[1]
24                    
25                    if next_row < 0 or next_col < 0 or next_row > nrow - 1 or next_col > ncol - 1:
26                        continue
27
28                    if grid[next_row][next_col] == 1:
29                        q.append((next_row, next_col))
30                        grid[next_row][next_col] = 2
31            step += 1
32        
33        
34        for i in range(nrow):
35            for j in range(ncol):
36                if grid[i][j] == 1:
37                    return -1
38
39        if step > 0:
40            return step - 1
41        else:
42            return 0
43
44        