# Last updated: 5/16/2026, 12:27:12 PM
class Solution:
    def maximumSwap(self, num: int) -> int:
        
        list_num = [int(item) for item in list(str(num))]

        mapping = {}
        for i in range(len(list_num)):
            mapping[list_num[i]] = i

        print(list_num)
        print(mapping)
        
        for i in range(len(list_num)):
            for digit in range(9, list_num[i], -1):
                if digit in mapping and mapping[digit] > i:
                    ind = mapping[digit]

                    print(ind, i)
                    list_num[ind], list_num[i] = list_num[i], list_num[ind]
                    

                    return int(''.join([str(item) for item in list_num]))

        return num