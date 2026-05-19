# Last updated: 5/18/2026, 11:04:00 PM
1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        
4        nums.sort()
5
6        self.res = []
7        self.track = []
8
9        self.backtrack(nums, 0)
10        return self.res
11
12
13    def backtrack(self, nums, start):
14
15        self.res.append(self.track.copy())
16
17
18        for i in range(start, len(nums)):
19
20            if i > start and nums[i] == nums[i-1]:
21                continue
22
23            self.track.append(nums[i])
24            self.backtrack(nums, i+1)
25            self.track.pop()
26
27                
28        