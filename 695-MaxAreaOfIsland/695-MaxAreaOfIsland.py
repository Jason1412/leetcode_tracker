# Last updated: 5/16/2026, 12:27:07 PM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        self.area = 0

        max_area = 0

        nrow, ncol = len(grid), len(grid[0])

        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    if max_area < self.area:
                        max_area = self.area
                    self.area = 0

        return max_area
    

    def dfs(self, grid, i, j):


        if grid[i][j] == 0:
            return


        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        grid[i][j] = 0
        self.area += 1

        for d in dirs:
            x = i + d[0]
            y = j + d[1]

            if not self.valid(grid, x, y):
                continue
            
            self.dfs(grid, x, y)


    def valid(self, grid, i, j):

        nrow, ncol = len(grid), len(grid[0])

        if 0 <= i <= nrow - 1 and 0 <= j <= ncol - 1:
            return True
        return False



































    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     nrow, ncol = len(grid), len(grid[0])


    #     self.dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    #     self.max_area = 0

    #     res = 0

    #     for i in range(nrow):
    #         for j in range(ncol):
    #             if grid[i][j] == 1:
    #                 self.fillIsland(grid, i, j)
    #                 if self.max_area > res:
    #                     res = self.max_area
    #                 self.max_area = 0
    #     return res



    # def fillIsland(self, grid, i, j):

    #     nrow, ncol = len(grid), len(grid[0])

    #     if i < 0 or i > nrow - 1 or j < 0 or j > ncol - 1:
    #         return 

    #     if grid[i][j] == 0:
    #         return 

    #     grid[i][j] = 0

    #     self.max_area += 1
    #     for d in self.dirs:
    #         self.fillIsland(grid, i + d[0], j + d[1])