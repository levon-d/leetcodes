# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        
        if not head.next.next:
            temp = head.next
            temp.next = head 
            head.next = None
            return temp 
        
        left = None 
        right = head 

        while right: 
            next_node = right.next 
            right.next = left 
            left = right 
            right = next_node 

        return left
