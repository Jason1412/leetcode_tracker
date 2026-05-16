# Last updated: 5/16/2026, 12:29:01 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        count = 0

        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)

                    count += 1

        return count


    def dfs(self, grid, i, j):
        
        if not self.valid(grid, i, j) or grid[i][j] == "0":
            return

        grid[i][j] = "0"

        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


    def valid(self, grid, i, j):
        nrow, ncol = len(grid), len(grid[0])

        if 0 <= i <= nrow-1 and 0 <= j <= ncol-1:
            return True
        return False