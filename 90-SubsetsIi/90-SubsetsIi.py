# Last updated: 5/16/2026, 12:30:05 PM
class Solution:
# Method 3 =======================================================
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        combination = []
        combinations = []

        refuse = False
        nums.sort()

        self.helper(nums, 0, combinations, combination, refuse)

        return combinations


    def helper(self, nums, start, combinations, combination, refuse):


        if start == len(nums):
            combinations.append(combination.copy())
            return

        #　即将要选number进来combination的时候, 进行判断.
        if refuse and nums[start] == nums[start-1]:
            self.helper(nums, start+1, combinations, combination, True)
            return
        
        combination.append(nums[start])
        self.helper(nums, start+1, combinations, combination, False)
        combination.pop()

        # 先考虑不选number的情形
        self.helper(nums, start+1, combinations, combination, True)









# Method 2 =======================================================
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
    #     # used = [False for _ in range(len(nums))]

    #     self.res = []
    #     self.track = []

    #     nums.sort()

    #     self.dfs(nums, 0)

    #     return self.res


    # def dfs(self, nums, start):
        
    #     self.res.append(self.track[:])

    #     for i in range(start, len(nums)):
            

    #         if i > start and nums[i] == nums[i-1]:
    #             continue

    #         self.track.append(nums[i])
    #         # used[i] = True

    #         self.dfs(nums, i + 1)

    #         # used[i] = False
    #         self.track.pop()



# Method 1 ====================================================

    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
    #     used = [False for _ in range(len(nums))]

    #     self.res = []
    #     self.track = []

    #     nums.sort()

    #     self.dfs(nums, used, 0)

    #     return self.res


    # def dfs(self, nums, used, start):
        
    #     self.res.append(self.track[:])

    #     for i in range(start, len(nums)):
            

    #         if i > 0 and not used[i-1] and nums[i] == nums[i-1]:
    #             continue

    #         self.track.append(nums[i])
    #         used[i] = True

    #         self.dfs(nums, used, i + 1)

    #         used[i] = False
    #         self.track.pop()

