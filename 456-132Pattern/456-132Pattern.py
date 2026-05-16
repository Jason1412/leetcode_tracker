# Last updated: 5/16/2026, 12:27:54 PM
import sys
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        max_2nd = -sys.maxsize

        for i in range(len(nums)-1, -1, -1):

            if nums[i] < max_2nd:
                return True

            while stack and nums[i] > stack[-1]:
                max_2nd = stack.pop()

            stack.append(nums[i])
        
        return False
