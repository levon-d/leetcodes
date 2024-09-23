# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        
        originalOdd = head 
        originalEven = head.next

        currentOdd = head
        currentEven = head.next 

        while currentEven and currentEven.next and currentOdd and currentOdd.next: 
            prevEven = currentEven
            prevOdd = currentOdd
            currentEven = currentEven.next.next
            currentOdd = currentOdd.next.next 
            
            prevEven.next = currentEven 
            prevOdd.next = currentOdd 

        currentOdd.next = originalEven

        return originalOdd 
