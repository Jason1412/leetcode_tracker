# Last updated: 5/16/2026, 12:30:33 PM
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        n1 = len(num1)
        n2 = len(num2)
        nums = [0 for _ in range(n1+n2)]

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                prod = int(num1[i]) * int(num2[j])

                tmp = prod + nums[i+j+1]

                single = tmp % 10
                ten = tmp // 10
                
                nums[i+j+1] = single
                nums[i+j] += ten

                # if nums[i+j] > 10:
                #     print("e!!!!")
                #     nums[i+j] = nums[i+j] % 10
                #     nums[i+j-1] = nums[i+j-1] // 10
        
        i = 0
        while i < len(nums) and nums[i] == 0:
            i += 1
        
        print("nums=", nums)

        res_str = ''.join(str(e) for e in nums[i:])
        return res_str if res_str else '0'
