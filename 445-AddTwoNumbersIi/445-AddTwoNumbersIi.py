# Last updated: 5/16/2026, 12:27:58 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rev_l1 = self.reverse(l1)
        rev_l2 = self.reverse(l2)

        dummy = ListNode()
        head = dummy
        add_one = 0

        while rev_l1 and rev_l2:
            tmp_sum = rev_l1.val + rev_l2.val + add_one
            # print("tmp_sum=", tmp_sum)

            single = tmp_sum % 10 
            
            add_one = tmp_sum // 10

            head.next = ListNode(single)

            head = head.next
            rev_l1 = rev_l1.next
            rev_l2 = rev_l2.next


        # print("rev_l1=", rev_l1)
        # print("rev_l2=", rev_l2)
        # print("add_one=", add_one)

        while rev_l1:
            tmp_sum = rev_l1.val + add_one

            single = tmp_sum % 10
            
            add_one = tmp_sum // 10

            head.next = ListNode(single)
            head = head.next
            rev_l1 = rev_l1.next

        while rev_l2:
            tmp_sum = rev_l2.val + add_one

            single = tmp_sum % 10 
            
            add_one = tmp_sum // 10

            head.next = ListNode(single)
            head = head.next
            rev_l2 = rev_l2.next


        # print("add_one=", add_one)
        if rev_l1 is None and rev_l2 is None and add_one == 1:
            head.next = ListNode(1)
        


        out = self.reverse(dummy.next)
        return out

        

            


    def reverse(self, head):

        prev = None
        while head:
            tmp = head.next
            head.next = prev

            prev = head
            head = tmp

        return prev  
