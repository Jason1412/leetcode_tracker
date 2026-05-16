# Last updated: 5/16/2026, 12:28:15 PM
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        nrow, ncol = len(matrix), len(matrix[0])

        pq = []

        for i in range(nrow):
            pq.append((matrix[i][0], i, 0))

        heapq.heapify(pq)

        res = None

        while pq and k > 0:
            min_val, i, j = heapq.heappop(pq)
            
            k -= 1
            if j+1 < ncol:
                heapq.heappush(pq, (matrix[i][j+1], i, j+1))

        res = min_val
        return res