# Last updated: 5/16/2026, 12:25:28 PM

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        

        count_diff = 0
        ind = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count_diff += 1
                ind.append(i)


        list_s1 = list(s1)
        list_s2 = list(s2)

        if count_diff == 0:
            return True
        elif count_diff == 2:
            list_s1[ind[0]], list_s1[ind[1]] = list_s1[ind[1]], list_s1[ind[0]]
            if ''.join(list_s1) == ''.join(list_s2):
                return True
            else:
                return False
        else:
            return False


