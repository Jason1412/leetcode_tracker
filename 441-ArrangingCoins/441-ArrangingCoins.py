# Last updated: 5/16/2026, 12:28:00 PM
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp_sum = 0
        ind = 0
        while (tmp_sum <= n):
            ind += 1
            tmp_sum = tmp_sum + ind
        
        return (ind-1)