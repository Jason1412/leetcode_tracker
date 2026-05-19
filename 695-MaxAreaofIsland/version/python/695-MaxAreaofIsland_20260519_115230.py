# Last updated: 5/19/2026, 11:52:30 AM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        
4        max_area = 0 
5        nrow, ncol = len(grid), len(grid[0])
6        self.islandArea = 0
7
8        for i in range(nrow):
9            for j in range(ncol):
10                if grid[i][j] == 1:
11                    
12                    self.dfs(grid, i, j)
13                    max_area = max(max_area, self.islandArea)
14                    self.islandArea = 0
15        return max_area
16
17
18
19
20    def dfs(self, grid, i, j):
21        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
22
23        nrow, ncol = len(grid), len(grid[0])
24
25        if i < 0 or j < 0 or i > nrow - 1 or j > ncol - 1:
26            return
27
28        if grid[i][j] == 0:
29            return
30
31
32        grid[i][j] = 0
33        self.islandArea += 1
34
35        for d in dirs:
36            new_i = i + d[0]
37            new_j = j + d[1]
38            self.dfs(grid, new_i, new_j)
39
40