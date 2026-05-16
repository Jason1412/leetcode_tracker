# Last updated: 5/16/2026, 12:30:52 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        nums.sort()

        out_three = []
        i = 0
        while i < len(nums)-2:
            while (i > 0 and i < len(nums)-2 and nums[i] == nums[i-1]):
                i += 1
            
            out_two = self.twoSum(nums, i+1, len(nums)-1, 0-nums[i])

            for item in out_two:
                out_three.append([nums[i]] + item)

            i += 1

            # while (i < len(nums)-2 and nums[i] == nums[i-1]):
            #     i += 1
            

        return out_three
        

        # Original logic to dedupe -----------------------------------
        # tmp = set(tuple(x) for x in out_three)
        # return [list(item) for item in tmp]


    
    def twoSum(self, nums, start, end, target):

        start = start
        end = end

        out = []
        while start < end:
            low = nums[start]
            high = nums[end]

            if low + high == target:
                out.append([low, high])
                while (start < end and nums[start] == low):
                    start += 1
                while (start < end and nums[end] == high):
                    end -= 1
            elif low + high < target:
                while (start < end and nums[start] == low):
                    start += 1
            elif low + high > target:
                while (start < end and nums[end] == high):
                    end -= 1

        
        return out
            


    





























    #     nums.sort()
    #     # print("nums=", nums)
    #     res_3sum = []
        
    #     i = 0
    #     # for i in range(len(nums)):
    #     while (i < len(nums)):
    #         res_2sum = self.twoSum(nums, i+1, 0 - nums[i])
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
        
