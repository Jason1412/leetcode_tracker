# Last updated: 5/16/2026, 12:30:27 PM
class Solution:
# Method 2 ======================
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        tmp = x

        while n != 0:
            if n % 2 == 1:
                res *= tmp
            tmp *= tmp
            n = n // 2
        return res
        


# Method 1 ==========================================
# O(n)
    # def myPow(self, x: float, n: int) -> float:
        
    #     if n == 0:
    #         return 1

    #     if n < 0:
    #         x = 1 / x
    #         n = -n

    #     res = 0

    #     for i in range(n):
    #         if i == 0:
    #             res = x
    #         else:
    #             res = res * x

    #     return res
