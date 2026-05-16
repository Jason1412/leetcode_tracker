# Last updated: 5/16/2026, 12:27:35 PM
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rec = {'A':0, 'L':0, 'P':0}
        
        if len(s) == 1:
            return True
        
        for i in range(len(s)):
            rec[s[i]] += 1
            
        if rec['A'] > 1:
            return False
        elif rec['L'] > 2:
            return not self.checkContL(s)
        else:
            return True
    
    def checkContL(self, s):
        nxt = 2
        cur = 1
        prev = 0
        while nxt <= len(s)-1:
            if s[cur] == 'L' and s[nxt] == 'L' and s[prev] == 'L':
                return True
            nxt += 1
            cur += 1
            prev += 1
        return False
            