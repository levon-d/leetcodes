class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        current = head 
        nextNode = head.next 
        dummy = ListNode(val=-200, next=current)
        prev = dummy 

        while nextNode: 
            if current.val != nextNode.val: 
                current = current.next
                nextNode = nextNode.next 
                prev = prev.next 
                continue 

            while nextNode and current.val == nextNode.val: 
                nextNode = nextNode.next 
                
            prev.next = nextNode 
            current = nextNode 
            nextNode = None if not current else current.next

        return dummy.next 

            


