# Last updated: 5/16/2026, 12:30:10 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        track = []
        combinations = []

        self.helper(nums, 0, track, combinations)

        return combinations


    def helper(self, nums, start, track, combinations):

        if start == len(nums):
            combinations.append(track.copy())

        if start == len(nums):
            return


        track.append(nums[start])
        self.helper(nums, start+1, track, combinations)

        track.pop()
        self.helper(nums, start+1, track, combinations)
        

# Method 1 ==============================================
    # def subsets(self, nums: List[int]) -> List[List[int]]:
        
    #     self.res = []

    #     self.track = []
    #     self.dfs(nums, 0)

    #     return self.res


    # def dfs(self, nums, start):

    #     # if start >= len(nums):
    #     #     return
    #     # Warning: results加入是在下一次dfs开始之后, 所以
    #     #　i = 2之后i = 3时，最后一组results才被加入进来
    #     self.res.append(self.track.copy())

    #     for i in range(start, len(nums)):
    #         self.track.append(nums[i])

    #         self.dfs(nums, i+1)

    #         self.track.pop()
