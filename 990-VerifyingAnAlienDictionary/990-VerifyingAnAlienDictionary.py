# Last updated: 5/16/2026, 12:26:17 PM
class Solution:
# Method 2 ============================================================
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mappings = {}
        for i in range(len(order)):
            mappings[order[i]] = i
            
        for i in range(1, len(words)):
            if not self.compare(words[i-1], words[i], mappings):
                return False
        
        return True
        

    def compare(self, word1, word2, mappings):

        n1, n2 = len(word1), len(word2)

        i, j = 0, 0
        while (i < n1 and j < n2):
            if word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                if mappings[word1[i]] > mappings[word2[j]]:
                    return False
                else:
                    return True
        
        if i < n1:
            return False

        return True





# Method 1 ===========================================================
    # def isAlienSorted(self, words: List[str], order: str) -> bool:
        
    #     mappings = {}
    #     for i in range(len(order)):
    #         mappings[order[i]] = i

    #     for i in range(1, len(words)):
    #         if self.serialize(words[i-1], mappings) > self.serialize(words[i], mappings):
    #             return False

    #     return True 

    
    # def serialize(self, string, mappings):

    #     out = []
    #     for c in string:
    #         tmp_str = str(mappings[c])
    #         if len(tmp_str) == 1:
    #             tmp_str = '0' + tmp_str
    #         out.append(tmp_str)
        
    #     return '-'.join(out)