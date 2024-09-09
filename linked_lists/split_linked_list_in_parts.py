# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        current, count = head, 0
        while current:
            current = current.next
            count += 1

        current = head
        result = [None] * k
        division = count // k
        remainder = count % k

        for i in range(k):
            dummy = ListNode(-1)
            current_size = division
            if remainder > 0:
                current_size += 1
                remainder -= 1

            tail = dummy

            for j in range(current_size):
                tail.next = ListNode(current.val)
                current, tail = current.next, tail.next

            result[i] = dummy.next

        return result
