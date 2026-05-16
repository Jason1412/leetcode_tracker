# Last updated: 5/16/2026, 12:29:31 PM
class Solution:
    
    
    def CalPalin(self, s):
        
        n = len(s)
        
        palin_mat = [[False for i in range(n)] for i in range(n)]
        
        for p in range(n):
            i = j = p
            while (i >= 0 and j < n and s[i] == s[j]):
                palin_mat[i][j] = True
                i -= 1
                j += 1
        
        for p in range(n-1):
            i = p
            j = p + 1
            while (i >= 0 and j < n and s[i] == s[j]):
                palin_mat[i][j] = True
                i -= 1
                j += 1
                        
        return palin_mat
                
    
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # state: minimum cuts needed for the string at i
        # f[i] = OR(f[j]+1, j < i and j+1~i is a palindrome)
        # 
        length = len(s)
        mat_pal = self.CalPalin(s)
        
        f = [i-1 for i in range(length+1)] # f[0] --- s = []
                                           # f[1] --- s = [a]
                                           # length of f = length of s + 1
        
        for i in range(2,length+1):
            for j in range(i):
                if mat_pal[j][i-1] and f[j]+ 1 < f[i]: # Why we use [j][i-1], because len(f) = len(s) + 1
                    f[i] = f[j] + 1 # if j = 0, f[i] should be 0; if j != 0, f[i] should be f[j] + 1 
                    if f[i] == 0:
                        break
        return f[length]
        
        # Easier to think if put the cut point between the digit
        
        