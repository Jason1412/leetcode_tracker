# Last updated: 5/16/2026, 12:27:33 PM
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count = {}
#         count[0] = 1

#         n = len(nums)

#         res = 0

#         sum_i = 0 # 相当于一个preSum array
#         sum_j = 0

#         for i in range(n):
#             sum_i += nums[i]

#             sum_j = sum_i - k

#             if sum_j in count:
#                 res += count[sum_j]

#             count[sum_i] = count.get(sum_i, 0) + 1

#         return res



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = {}
        count[0] = 1
        n = len(nums)

        res = 0
        preSum = [0 for _ in range(n+1)]

        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]
            
            need = preSum[i+1] - k

            if need in count:
                res += count[need]

            count[preSum[i+1]] = count.get(preSum[i+1], 0) + 1

        return res





























    # def subarraySum(self, nums: List[int], k: int) -> int:
        
    #     preSum = {}
    #     preSum[0] = 1

    #     res = 0
    #     sum_i = 0

    #     for i in range(len(nums)):
    #         sum_i = sum_i + nums[i]

    #         sum_j = sum_i - k

    #         if sum_j in preSum:
    #             res += preSum[sum_j]
            
    #         # if sum_i not in preSum:
    #         #     preSum[sum_i] = 1
    #         # else:
    #         #     preSum[sum_i] += 1

    #         preSum[sum_i] = preSum.get(sum_i, 0) + 1

    #     return res

