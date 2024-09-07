# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def checkPath(linkedListNode, treeRoot): 
            if not linkedListNode:
                return True 
            if not treeRoot:
                return False

            if linkedListNode.val != treeRoot.val:
                return False 

            return checkPath(linkedListNode.next, treeRoot.left) or checkPath(linkedListNode.next, treeRoot.right)

        queue = deque([root])

        while queue:
            current = queue.popleft()
            if current.val == head.val and checkPath(head, current):
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return False 

