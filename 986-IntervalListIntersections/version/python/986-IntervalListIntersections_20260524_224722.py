# Last updated: 5/24/2026, 10:47:22 PM
1class Solution:
2    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
3        
4        i, j = 0, 0
5
6        res = []
7        while i < len(firstList) and j < len(secondList):
8            a1, a2 = firstList[i][0], firstList[i][1]
9            b1, b2 = secondList[j][0], secondList[j][1]
10
11            if b2 >= a1 and b1 <= a2:
12                res.append([max(a1, b1), min(a2, b2)])
13
14            if b2 < a2:
15                j += 1
16            else:
17                i += 1
18
19        return res
20
21