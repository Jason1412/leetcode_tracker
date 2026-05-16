# Last updated: 5/16/2026, 12:30:03 PM
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        
        if n1 + n2 != n3:
            return False
        
        if n1 == 0 and s2 != s3:
            return False
        if n2 == 0 and s1 != s3:
            return False
        
        f = [[False]*(n2+1) for i in range(n1+1)]
        
        f[0][0] = True
        
        for i in range(n1):
            f[i+1][0] = (s1[:i+1] == s3[:i+1])
        
        for i in range(n2):
            f[0][i+1] = (s2[:i+1] == s3[:i+1])
            
        for i in range(n1):
            for j in range(n2):
                
                if (s1[i] == s3[i+j+1] and f[i][j+1]) or (s2[j] == s3[i+j+1] and f[i+1][j]):
                    f[i+1][j+1] = True
        return f[n1][n2]
                