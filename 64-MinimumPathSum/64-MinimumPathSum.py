# Last updated: 5/16/2026, 12:30:20 PM
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i-1][j]
                elif i > 0 and j > 0:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
                
        return grid[i][j]