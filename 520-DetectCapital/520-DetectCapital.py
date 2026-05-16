# Last updated: 5/16/2026, 12:27:46 PM
class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if word.isupper() or word.islower():
            return True
        elif len(word) > 1 and word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
        
                
        