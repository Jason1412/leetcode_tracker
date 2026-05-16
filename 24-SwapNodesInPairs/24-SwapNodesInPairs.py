# Last updated: 5/16/2026, 12:30:45 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head

        first = head
        second = head.next
        suffix = self.swapPairs(second.next)

        second.next = first
        first.next = suffix

        return second