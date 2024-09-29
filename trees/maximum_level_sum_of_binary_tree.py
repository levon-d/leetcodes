# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1

        queue = deque([root])
        maximum = float("-inf")
        current_level = 0
        result = 1

        while queue:
            current_level_sum = 0
            current_level += 1
            length = len(queue)

            for i in range(length):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                current_level_sum += node.val

            if current_level_sum > maximum:
                result = current_level
                maximum = current_level_sum

        return result
