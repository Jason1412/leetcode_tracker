# Last updated: 5/16/2026, 12:25:41 PM
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        self.dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(nrow):
            if grid[i][0] == 0:
                self.fillIsland(grid, i, 0)
            if grid[i][ncol-1] == 0:
                self.fillIsland(grid, i, ncol-1)

        for j in range(ncol):
            if grid[0][j] == 0:
                self.fillIsland(grid, 0, j)
            if grid[nrow-1][j] == 0:
                self.fillIsland(grid, nrow-1, j)

        
        count = 0
        for i in range(1, nrow-1):
            for j in range(1, ncol-1):
                if grid[i][j] == 0:
                    self.fillIsland(grid, i, j)
                    count += 1

        return count


    def fillIsland(self, grid, i, j):
        nrow = len(grid)
        ncol = len(grid[0])

        if i < 0 or i > (nrow - 1) or j < 0 or j > (ncol - 1):
            return

        if grid[i][j] == 1:
            return

        grid[i][j] = 1 # !!!

        for d in self.dirs:
            
            self.fillIsland(grid, i + d[0], j + d[1])

        