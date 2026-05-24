# Last updated: 5/23/2026, 10:50:10 PM
1class Solution:
2    def customSortString(self, order: str, s: str) -> str:
3        
4        s_dict = {}
5        for c in s:
6            if c not in s_dict:
7                s_dict[c] = 1
8            else:
9                s_dict[c] += 1
10
11        res = ''
12        for c_order in order:
13            if c_order in s_dict:
14                res += c_order * s_dict[c_order]
15                del s_dict[c_order]
16
17        for c, count in s_dict.items():
18            res += c * count
19
20        return res