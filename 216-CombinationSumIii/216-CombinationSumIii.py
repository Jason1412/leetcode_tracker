# Last updated: 5/16/2026, 12:28:55 PM
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i+1 for i in range(9)]

        self.res = []
        self.track = []

        self.dfs(nums, 0, n, 0, 0, k)

        return self.res



    def dfs(self, nums, start, target, cumSum, cumCount, k):

        if cumSum == target and cumCount == k:
            self.res.append(self.track.copy())
            return

        if cumSum > target or cumCount > k:
            return

        
        for i in range(start, len(nums)):

            self.track.append(nums[i])
            cumSum += nums[i]
            cumCount += 1

            self.dfs(nums, i+1, target, cumSum, cumCount, k)

            cumCount -= 1
            cumSum -= nums[i]
            self.track.pop()

        