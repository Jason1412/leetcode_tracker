# Last updated: 5/16/2026, 12:30:47 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = list1
        p2 = list2

        dummy = ListNode(-1)
        head = dummy

        while p1 and p2:
            if p1.val < p2.val:
                head.next = p1
                head = head.next
                p1 = p1.next
            else:
                head.next = p2
                head = head.next
                p2 = p2.next
                
        if p1 is None:
            head.next = p2
        
        if p2 is None:
            head.next = p1

        return dummy.next