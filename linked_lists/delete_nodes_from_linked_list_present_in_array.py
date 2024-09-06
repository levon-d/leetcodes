class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head) 
        prev = dummy 
        current = head 
        nums = set(nums)
        while current: 
            while current and current.val in nums:
                current = current.next 
            prev.next = current 
            prev = current 
            current = None if not current else current.next 
        return dummy.next 
