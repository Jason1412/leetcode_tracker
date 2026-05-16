# Last updated: 5/16/2026, 12:27:51 PM
class Solution:
# Method 2 ==========================================================
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dd = {}
        result = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dd.setdefault((i+j), []).append(mat[i][j])

        for k, v in dd.items():
            if k % 2 == 0:
                v.reverse()

            result += v
        return result






# Method 1 ==========================================================
    # def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    #     nrow, ncol = len(mat), len(mat[0])

    #     i = 0
    #     j = 0

    #     out = []
    #     out.append(mat[i][j])
    #     flag = 'down'

    #     while self.valid_index(i, j, mat):
            
    #         if flag == 'down':
    #             if j < ncol-1:
    #                 j += 1
    #             else:
    #                 i += 1
    #             print(i, j)
    #             tmp, prev_i, prev_j = self.collect_diag(i, j, mat, flag)
    #             out.extend(tmp)
    #             i, j = prev_i, prev_j
    #             flag = 'up'
    #             continue

    #         if flag == 'up':
    #             if i < nrow - 1:
    #                 i += 1
    #             else:
    #                 j += 1
    #             print(i, j)
    #             tmp, prev_i, prev_j = self.collect_diag(i, j, mat, flag)
    #             out.extend(tmp)
    #             i, j = prev_i, prev_j
    #             flag = 'down'
    #             continue

    #     return out

            
    # def valid_index(self, i, j, mat):
    #     nrow, ncol = len(mat), len(mat[0])

    #     if 0 <= i <= nrow-1 and 0 <= j <= ncol-1:
    #         return True
    #     return False


    # def collect_diag(self, i, j, mat, flag):
    #     out = []
    #     prev_i, prev_j  = i, j
    
   
    #     if flag == "down":
    #         while self.valid_index(i, j, mat):
    #             out.append(mat[i][j])
    #             prev_i = i
    #             prev_j = j
    #             i += 1
    #             j -= 1

    #     if flag == "up":
    #         while self.valid_index(i, j, mat):
    #             out.append(mat[i][j])
    #             prev_i = i
    #             prev_j = j
    #             i -= 1
    #             j += 1

    #     return out, prev_i, prev_j