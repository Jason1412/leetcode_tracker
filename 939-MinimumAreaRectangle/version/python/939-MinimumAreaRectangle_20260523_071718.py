# Last updated: 5/23/2026, 7:17:18 AM
1class Solution:
2    def minAreaRect(self, points: List[List[int]]) -> int:
3        pts_set = set(map(tuple, points))
4
5        min_area = float('inf')
6        for i, p2 in enumerate(points):
7            for j in range(i):
8                p1 = points[j]
9                if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in pts_set and (p2[0], p1[1]) in pts_set:
10                    temp_area = abs((p2[0] - p1[0]) * (p2[1] - p1[1]))
11                    min_area = min(min_area, temp_area)
12
13
14        return min_area if min_area < float('inf') else 0
15