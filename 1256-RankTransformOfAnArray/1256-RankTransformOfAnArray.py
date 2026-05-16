# Last updated: 5/16/2026, 12:25:45 PM
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        arr_copy = arr.copy()

        arr_copy.sort()

        rank = 1

        dict_num = {}
        for i in range(len(arr_copy)):
            
            if arr_copy[i] in dict_num:
                continue

            dict_num[arr_copy[i]] = rank
            rank += 1

        
        return [dict_num[num] for num in arr]


