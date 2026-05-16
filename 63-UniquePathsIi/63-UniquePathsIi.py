# Last updated: 5/16/2026, 12:30:21 PM
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        num_map = {}
        if obstacleGrid[0][0] == 1:
            num_map[(0,0)] = 0
        else:
            num_map[(0,0)] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    if obstacleGrid[i][j] == 1:
                        num_map[(i,j)] = 0
                    else:
                        num_map[(i,j)] = num_map[(i,j-1)]
                elif j == 0 and i > 0:
                    if obstacleGrid[i][j] == 1:
                        num_map[(i,j)] = 0
                    else:
                        num_map[(i,j)] = num_map[(i-1,j)]
                elif i > 0 and j > 0:
                    if obstacleGrid[i][j] == 1:
                        num_map[(i,j)] = 0
                    else:
                        num_map[(i,j)] = num_map[(i-1,j)] + num_map[(i,j-1)]
        
        return num_map[(m-1,n-1)]
                