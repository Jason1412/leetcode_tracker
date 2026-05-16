# Last updated: 5/16/2026, 12:26:49 PM
class Solution:
    rotate = '015--29-86'
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        for i in range(1,N+1):
            if self.isGood(i):
                cnt += 1
        return cnt
        
        
    def isGood(self, num):
        str_num = str(num)
        rotate_num = ''
        for num in str_num:
            tmp = self.rotate[int(num)]
            if tmp == '-':
                return False
            rotate_num += tmp
            
        if rotate_num != str_num:
            return True
        else:
            return False