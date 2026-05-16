# Last updated: 5/16/2026, 12:26:11 PM
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        preSum = [0 for _ in range(n+1)]

        count = {0:1}

        res = 0


        for i in range(1, n+1):
            preSum[i] = preSum[i-1] + nums[i-1]

            remainder = preSum[i] % k
            
            if remainder in count:
                res += count[remainder]
                count[remainder] += 1
            else:
                count[remainder] = 1

        return res            