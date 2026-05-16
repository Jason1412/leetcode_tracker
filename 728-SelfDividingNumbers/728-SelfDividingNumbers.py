# Last updated: 5/16/2026, 12:27:03 PM
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        out = []
        
        for num in range(left, right+1):
            ind = 1
            divisors = self.findDivider(num)
            # print('nums',num)
            for divisor in divisors:
                if divisor == 0:
                    ind = 0
                    break
                if num % divisor != 0:
                    ind = 0
                    break
            if ind == 1:
                out.append(num)
        return out
        
        
    def findDivider(self, num):
        
        out = []
        divisor = num
        while (divisor != 0):
            
            remainder = divisor % 10
            divisor = divisor // 10
            out.append(remainder)
            
        return out
        