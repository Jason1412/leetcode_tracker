# Last updated: 5/16/2026, 12:26:44 PM
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mose = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        
        word_mose_set = set()
        
        for word in words:
            tmp = []
            for char in word:
                tmp += mose[ord(char) - ord('a')]
            word_mose =  ''.join(tmp)
            word_mose_set.add(word_mose)
            
        return len(word_mose_set)