# Last updated: 5/16/2026, 12:25:25 PM
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        nrow, ncol = len(grid1), len(grid1[0])

        for i in range(nrow):
            for j in range(ncol):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    self.fillIsland(grid2, i, j)

        
        res = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid2[i][j] == 1:
                    res += 1
                    self.fillIsland(grid2, i, j)

        return res


    def fillIsland(self, grid, i, j):

        nrow, ncol = len(grid), len(grid[0])

        if i < 0 or i > nrow - 1 or j < 0 or j > ncol - 1:
            return 
        
        if grid[i][j] == 0:
            return

        
        grid[i][j] = 0

        self.fillIsland(grid, i + 1, j)
        self.fillIsland(grid, i - 1, j)
        self.fillIsland(grid, i, j + 1)
        self.fillIsland(grid, i, j - 1)

