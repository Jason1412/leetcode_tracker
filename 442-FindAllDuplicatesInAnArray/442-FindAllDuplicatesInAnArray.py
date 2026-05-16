# Last updated: 5/16/2026, 12:27:59 PM
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
            else:
                res.append(abs(num))

        return res