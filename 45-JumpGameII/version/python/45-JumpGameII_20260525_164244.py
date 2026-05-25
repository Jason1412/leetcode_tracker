# Last updated: 5/25/2026, 4:42:44 PM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        
4        if len(nums) == 1:
5            return 0
6
7        farthest = 0
8        end = 0
9        n = len(nums)
10        jumps = 0
11
12        for i in range(n):
13
14            farthest = max(nums[i] + i, farthest)
15
16            if i == end:
17                end = farthest
18                jumps += 1
19
20                if farthest >= n - 1:
21                    return jumps
22
23        return -1