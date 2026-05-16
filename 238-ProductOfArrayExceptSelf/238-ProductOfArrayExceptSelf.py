# Last updated: 5/16/2026, 12:28:45 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        preProd1 = [1 for _ in range(n+1)]
        preProd2 = [1 for _ in range(n+1)]

        for i in range(1, n+1):
            preProd1[i] = preProd1[i-1] * nums[i-1]

        for i in range(n-1, -1, -1):
            preProd2[i] = preProd2[i+1] * nums[i]

        print(preProd1)
        print(preProd2)
        
        for i in range(1, n+1):
            nums[i-1] = preProd1[i-1] * preProd2[i]

        return nums
