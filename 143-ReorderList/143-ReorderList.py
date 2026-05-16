# Last updated: 5/16/2026, 12:29:24 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        stack = []

        p = head
        while p is not None:
            stack.append(p)
            p = p.next

        p = head
        while p is not None:
            
            lastNode = stack.pop()

            nextNode = p.next
            if lastNode == nextNode or lastNode.next == nextNode:
                lastNode.next = None
                break

            
            p.next = lastNode
            lastNode.next = nextNode
            p = nextNode

        return head