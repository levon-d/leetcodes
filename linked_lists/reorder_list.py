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

        nodes = []
        l = 0 
        current = head 

        while current: 
            nodes.append(current)
            current = current.next 

        r = len(nodes)-1

        originalHead = head 
        current = head
        selectFromEnd = True 
        while l<=r:
            if selectFromEnd:
                current.next = nodes[r]
                l+=1 
                selectFromEnd = False
            else: 
                current.next = nodes[l]
                r-=1 
                selectFromEnd = True

            if l > r:
                current.next = None
            current = current.next 

        return originalHead

