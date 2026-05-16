# Last updated: 5/16/2026, 12:28:19 PM
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        d1 = {}
        d2 = {}
        
        for i in nums1:
            if i not in d1:
                d1[i] = 0
            d1[i] += 1
            
        for j in nums2:
            if j not in d2:
                d2[j] = 0
            d2[j] += 1
            
        # find the overlap of the two dictionaries
        keys1 = set(d1.keys())
        keys2 = set(d2.keys())
        
        intersection = keys1 & keys2
        
        print intersection
        
        output = []
        for item in list(intersection):
            print "item:", item
            times = min([d1[item], d2[item]])
            print "times:", times 
            print "term added:", d1[item]
            output.extend([item] * times)   # Warning: should put item here, not d1[item]
                    
        return output
        