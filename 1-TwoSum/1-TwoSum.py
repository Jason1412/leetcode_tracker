# Last updated: 5/16/2026, 12:30:56 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        valToIndex = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in valToIndex:
                return [valToIndex[need], i]
            
            valToIndex[nums[i]] = i
        return []


# Method 1 ======================================================
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    #     dict_num = {}

    #     for i, num in enumerate(nums):
    #         dict_num[num] = i

    #     for i, num in enumerate(nums):
    #         tmp = target - num
    #         if tmp in dict_num and dict_num[tmp] != i:
    #             return [i, dict_num[tmp]]

        