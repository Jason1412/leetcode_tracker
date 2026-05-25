# Last updated: 5/24/2026, 8:09:19 PM
1class Solution:
2    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
3        
4        intervals.sort(key=lambda x: (x[0], -x[1]))
5
6        left = intervals[0][0]
7        right = intervals[0][1]
8
9        num_merged = 0
10
11        for i in range(1, len(intervals)):
12            intv = intervals[i]
13
14            if intv[0] < right and intv[1] <= right:
15                num_merged += 1
16            if intv[0] < right and intv[1] > right:
17                right = intv[1]
18            if right < intv[0]:
19                left = intv[0]
20                right = intv[1]
21        
22        return len(intervals) - num_merged
23