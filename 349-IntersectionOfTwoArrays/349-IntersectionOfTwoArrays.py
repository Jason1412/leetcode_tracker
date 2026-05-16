# Last updated: 5/16/2026, 12:28:20 PM
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        tmp = set(nums1) & set(nums2)
        return list(tmp)