# Last updated: 5/16/2026, 12:26:39 PM
# Method 3 ==========================================================
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        N = len(grid)
        index = 2
        area = {}
        res = 0

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    area[index] = self.dfs(i, j, index, grid)
                    index += 1

        if area.values():
            res = max(area.values())

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    tmp_area = 0
                    tmp = [grid[x][y] for x, y in self.move(i, j, grid) if grid[x][y] != 0]
                    possible_ind = set(tmp)
                    # print(possible_ind)
                    if possible_ind:
                        tmp_area = sum(area[ind] for ind in possible_ind)
                    tmp_area += 1
                    res = max(res, tmp_area)
        return res





    def dfs(self, x, y, index, grid):

        area = 1
        grid[x][y] = index
        for i, j in self.move(x, y, grid):
            if grid[i][j] == 1:
                area += self.dfs(i, j, index, grid)
        return area


    def move(self, x, y, grid):
        N = len(grid)
        out = []
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + i < N and 0 <= y + j < N:
                out.append((x+i, y+j))
        return out


# Method 2 ==========================================================
# class Solution:
#     def largestIsland(self, grid: List[List[int]]) -> int:
#         def find_val(ref, grid, i, j):
#             if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or grid[i][j] == ref:
#                 return 0
#             grid[i][j] = ref
#             return 1 + (find_val(ref, grid, i+1, j) + find_val(ref, grid, i-1, j) + find_val(ref, grid, i, j+1) + find_val(ref, grid, i, j-1))

#         n = len(grid)
#         ref = 2
#         max_area = -1
#         mp = {}

#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     k = find_val(ref, grid, i, j)
#                     mp[ref] = k
#                     ref += 1
#                     max_area = max(max_area, k)

#         mp[0] = 0
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     sum_area = 0
#                     seen = set()
#                     if i > 0:
#                         seen.add(grid[i-1][j])
#                     if j > 0:
#                         seen.add(grid[i][j-1])
#                     if i < n-1:
#                         seen.add(grid[i+1][j])
#                     if j < n-1:
#                         seen.add(grid[i][j+1])
#                     for k in seen:
#                         sum_area += mp.get(k, 0)
#                     max_area = max(max_area, sum_area + 1)

#         return max_area




# Method 1 ===========================================================
# class Solution:
#     def largestIsland(self, grid: List[List[int]]) -> int:
#         res = 0        

#         nrow, ncol = len(grid), len(grid[0])


#         for i in range(nrow):
#             for j in range(ncol):
#                 if grid[i][j] == 0:

#                     # print("i, j={}{}".format(i, j))
#                     grid[i][j] = 1
#                     self.area = 0
#                     self.visited = [[False for _ in range(ncol)] for _ in range(nrow)]
#                     self.dfs(grid, i, j)
#                     grid[i][j] = 0
#                     res = max(res, self.area)
#                     # print("area = ", self.area)

#         if res == 0:
#             return nrow * ncol
#         else:
#             return res


#     def dfs(self, grid, i, j):

        
#         if not self.valid(grid, i, j):
#             return

#         if grid[i][j] == 0:
#             return

#         if self.visited[i][j]:

#             return

#         # grid[i][j] = 1
#         self.area += 1
#         self.visited[i][j] = True

#         self.dfs(grid, i+1, j)
#         self.dfs(grid, i-1, j)
#         self.dfs(grid, i, j+1)
#         self.dfs(grid, i, j-1)

    
        
#     def valid(self, grid, i, j):

#         nrow, ncol = len(grid), len(grid[0])

#         if 0 <= i <= nrow - 1 and 0 <= j <= ncol - 1:
#             return True
#         else:
#             return False