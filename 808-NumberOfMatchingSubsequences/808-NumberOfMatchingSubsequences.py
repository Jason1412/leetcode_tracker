# Last updated: 5/16/2026, 12:26:47 PM
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        
        s_dict = {}

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = [i]
            else:
                s_dict[s[i]].append(i)

        print(s_dict)

        count = 0
        for word in words:
            if self.isSubseq(s_dict, word):
                count += 1
        
        return count
        

    def isSubseq(self, s_dict, word):
        j = 0
        for i in range(len(word)):
            
            # print("char=", word[i])
            # print("j=", j)

            if word[i] not in s_dict:
                return False
            
            # If exists, find the first index >= j

            ind = self.bSearch(j, s_dict[word[i]])

            # print("ind=", ind)
            # print("----------------------")

            if ind == len(s_dict[word[i]])-1 and s_dict[word[i]][ind] < j:
                return False

            j = s_dict[word[i]][ind] + 1

            
        return True



    def bSearch(self, target, nums):

        # return the index of first element >= target in nums

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            
        if nums[start] >= target:
            return start
        else:
            return end
            



