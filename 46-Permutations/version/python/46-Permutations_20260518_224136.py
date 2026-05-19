# Last updated: 5/18/2026, 10:41:36 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        
4        self.res = []
5        self.track = []
6        self.used = [False] * len(nums)
7
8        self.backtrack(nums)
9
10        return self.res
11
12
13    def backtrack(self, nums):
14
15        if len(self.track) == len(nums):
16            self.res.append(self.track.copy())
17
18        
19        for i in range(len(nums)):
20            if self.used[i]:
21                continue
22
23            self.used[i] = True
24            self.track.append(nums[i])
25
26            self.backtrack(nums)
27
28            self.track.pop()
29            self.used[i] = False
30    