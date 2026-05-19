# Last updated: 5/19/2026, 11:33:16 AM
1DIRS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
2class Solution:
3    
4    def closedIsland(self, grid: List[List[int]]) -> int:
5        
6        count = 0
7
8        nrow, ncol = len(grid), len(grid[0])
9
10        for i in range(nrow):
11            if grid[i][0] == 0:
12                self.dfs(grid, i, 0)
13
14            if grid[i][ncol-1] == 0:
15                self.dfs(grid, i, ncol-1)
16
17        for j in range(ncol):
18            self.dfs(grid, 0, j)
19            self.dfs(grid, nrow-1, j)
20
21
22        for i in range(nrow):
23            for j in range(ncol):
24                if grid[i][j] == 0:
25                    count += 1
26                    self.dfs(grid, i, j)
27
28        return count
29
30    
31
32
33    def dfs(self, grid, i, j):
34        
35        nrow, ncol = len(grid), len(grid[0])
36
37        if i < 0 or j < 0 or i > nrow - 1 or j > ncol - 1:
38            return 
39
40        if grid[i][j] == 1:
41            return
42
43        
44        for d in DIRS:
45            new_i = i + d[0]
46            new_j = j + d[1]
47
48            grid[i][j] = 1
49
50            self.dfs(grid, new_i, new_j)