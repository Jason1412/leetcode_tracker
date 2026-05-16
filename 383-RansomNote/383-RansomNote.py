# Last updated: 5/16/2026, 12:28:12 PM
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        dict_ranNote = collections.Counter(ransomNote)
        dict_ranNote = dict(dict_ranNote)
        
        dict_magazine = collections.Counter(magazine)
        dict_magazion = dict(dict_magazine)
        
        list_ind = []
        for i in dict_ranNote.keys():
            if i in dict_magazine:
                if dict_magazine[i] >= dict_ranNote[i]:
                    list_ind.append(True)
                else:
                    list_ind.append(False)
            else:
                list_ind.append(False)
                
        if False in set(list_ind):
            return False
        else:
            return True