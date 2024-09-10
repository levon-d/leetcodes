# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        dummy = ListNode(val=-1, next=head)
        current=head 

        while current.next: 
            gcd = math.gcd(current.val,current.next.val)
            original_next = current.next 
            new_next = ListNode(val=gcd, next=original_next)
            current.next = new_next
            current = current.next.next

        return dummy.next 


        
