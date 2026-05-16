# Last updated: 5/16/2026, 2:23:34 PM
'''
NOTE:
- Need to pay attention to the position of "count"
- Number of visible people != number of people between itself and the next taller one.
'''

1class Solution:
2    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
3        
4        n = len(heights)
5
6        res = [0] * n
7        stack = []
8        
9        for i in range(n-1, -1, -1):
10            count = 0
11            while stack and heights[stack[-1]] < heights[i]:
12                stack.pop()
13                count += 1
14
15            # This part is important
16            if not stack:
17                res[i] = count   
18            else:
19                res[i] = count + 1
20                
21
22            stack.append(i)
23
24        return res
25