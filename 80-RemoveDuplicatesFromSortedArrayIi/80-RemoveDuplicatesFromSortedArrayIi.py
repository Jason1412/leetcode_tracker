# Last updated: 5/16/2026, 12:30:08 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        slow = 0
        fast = 0

        count = 0
        while fast < len(nums):

            
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            elif count < 2 and slow < fast:
                slow += 1
                nums[slow] = nums[fast]


            fast += 1
            count += 1

            if fast < len(nums) and nums[fast] != nums[fast-1]:
                count = 0

        return slow + 1