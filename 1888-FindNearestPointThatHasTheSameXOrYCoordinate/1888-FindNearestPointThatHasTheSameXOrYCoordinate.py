# Last updated: 5/16/2026, 12:25:29 PM
import sys
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDist = sys.maxsize
        ans = -1
        ind = -1

        for i in range(len(points)):
            pt_x = points[i][0]
            pt_y = points[i][1]
            if  pt_x == x or pt_y == y:
                manDist = abs(pt_x - x) + abs(pt_y - y)

                if manDist < minDist:
                    minDist = manDist
                    ind = i
        
        if minDist < sys.maxsize:

            return ind
        else:
            return -1
        