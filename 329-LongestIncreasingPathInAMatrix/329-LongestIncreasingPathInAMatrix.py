# Last updated: 5/16/2026, 12:28:26 PM
class Solution:
# Method 2 DP ============================================
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        nrow, ncol = len(matrix), len(matrix[0])

        points = []
        for i in range(nrow):
            for j in range(ncol):
                points.append((matrix[i][j], i, j))

        points.sort()

        res = {}

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(len(points)):
            key = (points[i][1], points[i][2])
            res[key] = 1

            for d in dirs:
                x = key[0] + d[0]
                y = key[1] + d[1]

                if not (0 <= x <= nrow - 1 and 0 <= y <= ncol - 1):
                    continue
                
                if points[i][0] > matrix[x][y]:
                    res[key] = max(res[key], res[(x,y)]+1)
        
        max_val = 0
        for val in res.values():
            if val > max_val:
                max_val = val
        return max_val

            







# Method 1 DFS ===========================================
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
    #     max_len = 0
    #     nrow, ncol = len(matrix), len(matrix[0])
    #     memo = [[-1 for _ in range(ncol)] for _ in range(nrow)]

    #     for i in range(nrow):
    #         for j in range(ncol):
    #             max_len = max(max_len, self.dfs(matrix, memo, i, j))
        
    #     # print("memo=", memo)
    #     return max_len


    # def dfs(self, matrix, memo, i, j):
        
    #     if memo[i][j] != -1:
    #         return memo[i][j]

    #     dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    #     count = 1
        
    #     for d in dirs:
    #         dx = d[0]
    #         dy = d[1]

    #         x = i + dx
    #         y = j + dy

    #         if not self.valid(matrix, x, y):
    #             continue

    #         if matrix[x][y] > matrix[i][j]:
    #             count = max(count, self.dfs(matrix, memo, x, y) + 1)

    #     memo[i][j] = count

    #     return count

    
    # def valid(self, matrix, i, j):
    #     nrow, ncol = len(matrix), len(matrix[0])

    #     if 0 <= i <= nrow-1 and 0 <= j <= ncol-1:
    #         return True
    #     else:
    #         return False
