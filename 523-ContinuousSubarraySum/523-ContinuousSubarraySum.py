# Last updated: 5/16/2026, 12:27:44 PM
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)

        if n < 2:
            return False

        val_to_ind = {0: -1}

        preSum = [0 for _ in range(n+1)]

        
        for i in range(1, n+1):
            preSum[i] = preSum[i-1] + nums[i-1]


        # for i in range(n):
            remainder = preSum[i] % k

            if remainder not in val_to_ind:
                val_to_ind[remainder] = i-1
            else:
                if i-1 - val_to_ind[remainder] > 1:
                    return True

        return False




























    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # n = len(nums)

        # preSum = [0 for _ in range(n+1)]

        # for i in range(1, n+1):
        #     preSum[i] = preSum[i-1] + nums[i-1]

        # val_to_ind = {0:-1}

        # for i in range(n):

        #     num_i = preSum[i+1] % k

        #     if num_i not in val_to_ind:
        #         val_to_ind[num_i] = i

        #     else:
        #         if i - val_to_ind[num_i] > 1:
        #             return True
        
        # return False

