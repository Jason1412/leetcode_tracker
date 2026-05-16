# Last updated: 5/16/2026, 12:30:04 PM
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def valid_ip(s):
            if len(s) == 0 or (len(s)>1 and s[0]=='0') or len(s) > 3:
                return False
            elif int(s) >= 0 and int(s) <= 255:
                return True
            else:
                return False
        
        if len(s) < 4 or len(s) > 12:
            return []
        out = []
        for i in range(3):
            if valid_ip(s[0:i+1]):
                for j in range(i+1,i+4):
                    if valid_ip(s[i+1:j+1]):
                        for k in range(j+1,j+4):
                            if valid_ip(s[j+1:k+1]) and valid_ip(s[k+1:]):
                                tmp = s[0:i+1] + "." + s[i+1:j+1] + "." + s[j+1:k+1] + "." + s[k+1:]
                                out.append(tmp)
        return out