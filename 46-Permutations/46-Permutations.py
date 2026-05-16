# Last updated: 5/16/2026, 12:30:30 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        self.track = []
        self.used = [False for _ in range(len(nums))]

        self.dfs(nums)

        return self.res


    def dfs(self, nums):
  
        if len(self.track) == len(nums):
            self.res.append(self.track.copy())

        for i in range(len(nums)):

            if self.used[i]:
                continue

            self.track.append(nums[i])
            self.used[i] = True

            self.dfs(nums)

            self.used[i] = False
            self.track.pop()

        