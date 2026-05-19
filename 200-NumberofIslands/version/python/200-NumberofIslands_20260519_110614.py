# Last updated: 5/19/2026, 11:06:14 AM
1dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
2
3class Solution:
4    def numIslands(self, grid: List[List[str]]) -> int:
5        
6        nrow, ncol = len(grid), len(grid[0])
7
8        count = 0
9        for i in range(nrow):
10            for j in range(ncol):
11                if grid[i][j] == '1':
12                    count += 1
13                    self.dfs(grid, i, j)
14
15        return count
16
17
18    def dfs(self, grid, i, j):
19
20        nrow, ncol = len(grid), len(grid[0])
21
22        if i < 0 or j < 0 or i > nrow - 1 or j > ncol - 1:
23            return
24
25        if grid[i][j] == '0':
26            return
27
28        for d in dirs:
29            new_i = i + d[0]
30            new_j = j + d[1]
31
32            grid[i][j] = '0'
33
34            self.dfs(grid, new_i, new_j)
35
36