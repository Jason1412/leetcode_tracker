# Last updated: 5/16/2026, 12:26:41 PM
class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        vowel = set('aeiouAEIOU')
        
        list_word = S.split(' ')
        
        out = []
        i = 1
        for word in list_word:
            if word[0] in vowel:
                tmp = word + 'ma' + 'a'*i
                out.append(tmp)
            else:
                tmp = word[1:] + word[0] + 'ma' + 'a'*i
                out.append(tmp)
            i += 1 
        return ' '.join(out)