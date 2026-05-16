# Last updated: 5/16/2026, 12:27:37 PM
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        nrow, ncol = len(mat), len(mat[0])

        queue = deque()
        out = [[-1 for _ in range(ncol)] for _ in range(nrow)]
        for i in range(nrow):
            for j in range(ncol):
                if mat[i][j] == 0:
                    out[i][j] = 0
                    queue.append((i, j))
                



        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:


            i, j = queue.popleft()

            for d in dirs:
                x = i + d[0]
                y = j + d[1]

                if 0 <= x <= nrow - 1 and 0 <= y <= ncol - 1 and out[x][y] == -1:
                    queue.append((x, y))
                    out[x][y] = out[i][j] + 1

        return out




# Method 1 =======================================================
# BFS from each point
    # def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
    #     nrow, ncol = len(mat), len(mat[0])

    #     out = [[-1 for _ in range(ncol)] for _ in range(nrow)]




    #     for i in range(nrow):
    #         for j in range(ncol):
    #             if mat[i][j] == 0:
    #                 out[i][j] = 0
    #             else:
    #                 out[i][j] = self.bfs(mat, i, j)

    #     return out



    # def bfs(self, mat, i, j):


    #     if mat[i][j] == 0:
    #         return 0

    #     depth = 0
    #     visited = set()

    #     queue = deque([(i, j)])
    #     visited.add((i, j))
        
    #     dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
    #     while queue:
            
    #         for _ in range(len(queue)):
    #             i, j = queue.popleft()
    #             if mat[i][j] == 0:
    #                 return depth

    #             for d in dirs:
    #                 x = i + d[0]
    #                 y = j + d[1]

    #                 if (x, y) in visited or not self.valid(mat, x, y):
    #                     continue

    #                 queue.append((x, y))    

    #         depth += 1


    # def valid(self, mat, x, y):
    #     nrow, ncol = len(mat), len(mat[0])

    #     if 0 <= x <= nrow - 1 and 0 <= y <= ncol - 1:
    #         return True
    #     return False


