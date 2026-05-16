# Last updated: 5/16/2026, 12:25:24 PM
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        nrow, ncol = len(maze), len(maze[0])

        visited = set()

        queue = deque()
        queue.append((entrance[0], entrance[1]))
        visited.add((entrance[0], entrance[1]))

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        depth = 0
        while queue:

            for _ in range(len(queue)):
                i, j = queue.popleft()

                if self.check_exit(maze, i, j, entrance):
                    return depth
                
                for d in dirs:
                    x = i + d[0]
                    y = j + d[1]

                    if not (0 <= x <= nrow-1 and 0 <= y <= ncol-1):
                        continue
                    if (x, y) in visited:
                        continue
                    if maze[x][y] == '+':
                        continue
                    
                    queue.append((x, y))
                    visited.add((x, y))

            depth += 1

        return -1




    def check_exit(self, maze, i, j, entrance):

        nrow, ncol = len(maze), len(maze[0])

        entr_i, entr_j = entrance[0], entrance[1]

        if i == entr_i and j == entr_j:
            return False

        if maze[i][j] == ".":
            if i == 0 or j == 0 or i == nrow - 1 or j == ncol - 1:
                return True
        
        return False
        
        