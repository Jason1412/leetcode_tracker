# Last updated: 5/16/2026, 12:26:10 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        left, right = 0, n - 1

        p = n - 1

        res = [0] * n

        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                res[p] = nums[right] ** 2
                right -= 1
            else:
                res[p] = nums[left] ** 2
                left += 1
            
            p -= 1
        
        return res



