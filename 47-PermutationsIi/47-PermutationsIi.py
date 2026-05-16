# Last updated: 5/16/2026, 12:30:29 PM
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        self.used = [False for _ in range(len(nums))]
        self.track = []
        self.res = []
        nums.sort()

        self.dfs(nums)

        return self.res
    

    def dfs(self, nums):

        if len(self.track) == len(nums):
            self.res.append(self.track.copy())
            
            return

        for i in range(len(nums)):

            if self.used[i]:
                continue 
            
            if i > 0 and not self.used[i-1] and nums[i] == nums[i-1]:
                continue
            
            self.track.append(nums[i])
            self.used[i] = True

            self.dfs(nums)

            self.used[i] = False
            self.track.pop()
            

