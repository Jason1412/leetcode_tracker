# Last updated: 5/16/2026, 12:27:55 PM
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        

        points.sort(key = lambda x: x[1])

        count = 1
        x_end = points[0][1]

        for point in points:
            start = point[0]
            if start > x_end:
                x_end = point[1]
                count += 1

        return count