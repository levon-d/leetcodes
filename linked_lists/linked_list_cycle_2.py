# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None 
            
        fast = head.next
        slow = head
        while slow != fast:
            slow = slow.next 
            if not fast.next or not fast.next.next:
                return None 
            fast = fast.next.next 

        slow = head 
        fast = fast.next

        while slow != fast:
            slow = slow.next 
            fast = fast.next 
        
        return fast 
