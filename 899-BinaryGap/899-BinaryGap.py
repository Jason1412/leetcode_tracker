# Last updated: 5/16/2026, 12:26:33 PM
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        loc = []
        
        distance = 0
        i = 1
        while(True):
            remainder = N % 2
            N = N // 2
            if remainder == 1:
                loc.append(i)
                
            if N == 0:
                break
            i += 1
        out = 0
        if len(loc) == 0 or len(loc) == 1:
            return 0
        else:
            for i in range(len(loc)-1):
                out = max(out, loc[i+1] - loc[i])
        return out