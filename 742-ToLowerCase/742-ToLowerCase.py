# Last updated: 5/16/2026, 12:27:01 PM
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        
        tmp = [chr(ord(i)+32) if ord(i) >= 65 and ord(i) <= 90 else i for i in str]
        
        return ''.join(tmp)