# Last updated: 5/16/2026, 12:25:22 PM
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        m = len(mat)
        n = len(mat[0])

        start = 0
        end = m - 1

        while (start + 1 < end):
            mid = (start + end) // 2

            max_col = self.max_ind(mat[mid])

            up, down = -1, -1

            if mid - 1 >= 0:
                up = mat[mid-1][max_col]

            if mid + 1 <= m - 1:
                down = mat[mid+1][max_col]
            
            if mat[mid][max_col] > up and mat[mid][max_col] > down:
                return [mid, max_col]
            elif mat[mid][max_col] < up:
                end = mid
            elif mat[mid][max_col] < down:
                start = mid

        
        max_col_s = self.max_ind(mat[start])
        max_col_e = self.max_ind(mat[end])

        if mat[start][max_col_s] > mat[end][max_col_e]:
            return [start, max_col_s]
        else:
            return [end, max_col_e]
    

    def max_ind(self, arr):
        max_val = arr[0]
        max_ind = 0

        for i, val in enumerate(arr):
            if val > max_val:
                max_val = val
                max_ind = i
        
        return max_ind