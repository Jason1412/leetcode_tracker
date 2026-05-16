# Last updated: 5/16/2026, 12:25:54 PM
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])

        if grid[0][0] == 1:
            return -1

        queue = deque([(0, 0)])
        visited = set()
        visited.add((0, 0))
        steps = 1

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if (i, j) == (nrow-1, ncol-1):
                    return steps

                for d in dirs:
                    x = i + d[0]
                    y = j + d[1]

                    if not self.check_valid(grid, x, y) or (x,y) in visited:
                        continue
                    
                    if grid[x][y] == 1:
                        continue
                    
                    queue.append((x, y))
                    visited.add((x, y))

            steps += 1

        return -1

    def check_valid(self, grid, x, y):
        nrow, ncol = len(grid), len(grid[0])

        if 0 <= x <= nrow-1 and 0 <= y <= ncol-1:
            return True
        return False
