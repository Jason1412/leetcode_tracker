# Last updated: 5/16/2026, 12:27:52 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res_nums2 = self.helper(nums2)

        mapping = {}

        for i in range(len(nums2)):
            mapping[nums2[i]] = res_nums2[i]

        out = []

        for num1 in nums1:
            out.append(mapping[num1])

        return out



    def helper(self, nums):

        n = len(nums)
        res = [0] * n
        stack = []

        for i in range(n-1, -1, -1):

            while stack and stack[-1] <= nums[i]:
                stack.pop()

            if not stack:
                res[i] = -1
            else:
                res[i] = stack[-1]

            stack.append(nums[i])

        return res