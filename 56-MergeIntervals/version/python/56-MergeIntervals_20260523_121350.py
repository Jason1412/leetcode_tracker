# Last updated: 5/23/2026, 12:13:50 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        
4
5        intervals.sort(key=lambda x: x[0])
6
7        res = []
8
9        res.append(intervals[0])
10
11        for i in range(1, len(intervals)):
12
13            cur = intervals[i]
14
15            last = res[-1]
16
17            if cur[0] <= last[1]:
18                last[1] = max(cur[1], last[1])
19            else:
20                res.append(cur)
21
22        return res
23