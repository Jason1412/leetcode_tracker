# Last updated: 5/16/2026, 12:30:50 PM
class Solution:

# Method 2 ===========================================================
# Recursive 

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        out = self.nSumTarget(nums, 4, 0, target)
        return out


    def nSumTarget(self, nums, n, start, target):
        # n --- n sum
        # start --- start index

        out = []
        sz = len(nums)

        if n < 2 or sz < n:
            return out

        if n == 2:
            res_2sum = self.twoSum(nums, start, target)
            return res_2sum

        else:
            i = start

            while (i < len(nums)):
                res_nsum = self.nSumTarget(nums, n-1, i+1, target - nums[i])
                for item in res_nsum:
                    item.append(nums[i])
                    out.append(item)
                i += 1
                while (i < len(nums) and nums[i] == nums[i-1]):
                    i += 1

        return out


    def twoSum(self, nums, start, target):
        # assume nums is sorted 
        left = start
        right = len(nums) - 1

        out = []
        while (left < right):
            low = nums[left]
            high = nums[right]

            if low + high == target:
                out.append([low, high])
                while (left < right and nums[left] == low):
                    left += 1
                while (left < right and nums[right] == high):
                    right -= 1

            elif low + high < target:
                left += 1
                while (left < right and nums[left] == low):
                    left += 1

            elif low + high > target:
                right -= 1
                while (left < right and nums[right] == high):
                    right -= 1
            
        return out





# Method 1 ===========================================================
# Leverage 3 sum algo

    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
    #     nums.sort()

    #     res_4sum = []

    #     i = 0
    #     while (i < len(nums)):
    #         res_3sum = self.threeSum(nums, i+1, target-nums[i])
    #         for item in res_3sum:
    #             item.append(nums[i])
    #             res_4sum.append(item)
    #         i += 1
    #         while (i < len(nums)-1 and nums[i] == nums[i-1]):
    #             i += 1
        
    #     return res_4sum


    # def threeSum(self, nums, start, target):
        
    #     # nums.sort()
    #     # print("nums=", nums)
    #     res_3sum = []
        
    #     i = start
    #     # for i in range(len(nums)):
    #     while (i < len(nums)):
    #         res_2sum = self.twoSum(nums, i+1, target - nums[i])
    #         for pair in res_2sum:
    #             pair.append(nums[i])
    #             res_3sum.append(pair)
    #         i += 1
    #         while (i < len(nums)-1 and nums[i] == nums[i-1]): 
    #             i += 1
    #         # print("i=", i)

    #     return res_3sum


    # def twoSum(self, nums, start, target):
    #     # assume nums is sorted 
    #     left = start
    #     right = len(nums) - 1

    #     out = []
    #     while (left < right):
    #         low = nums[left]
    #         high = nums[right]

    #         if low + high == target:
    #             out.append([low, high])
    #             while (left < right and nums[left] == low):
    #                 left += 1
    #             while (left < right and nums[right] == high):
    #                 right -= 1

    #         elif low + high < target:
    #             left += 1
    #             while (left < right and nums[left] == low):
    #                 left += 1

    #         elif low + high > target:
    #             right -= 1
    #             while (left < right and nums[right] == high):
    #                 right -= 1
            
    #     return out