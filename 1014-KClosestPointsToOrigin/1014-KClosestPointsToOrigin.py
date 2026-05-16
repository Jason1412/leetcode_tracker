# Last updated: 5/16/2026, 12:26:13 PM
from heapq import heappush, heappop, heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        if len(points) <= k:
            return points

        dists = [point[0] ** 2 + point[1] ** 2 for point in points]

        h = []
        for i in range(k):
            h.append((-dists[i], i))

        heapify(h)

        
        for i in range(k, len(dists)):

            heappush(h, (-dists[i], i))
            # print(h)
            heappop(h)
            # print(h)

        return [points[ind[1]] for ind in h]


