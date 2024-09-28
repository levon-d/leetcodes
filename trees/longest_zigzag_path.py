# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        if not root.left and not root.right:
            return 0

        def dfs(current_length, current_dir, current_node):
            if not current_node:
                self.result = max(self.result, current_length)
                return

            if current_dir == 0:
                dfs(current_length + 1, 1, current_node.left)
                dfs(0, 0, current_node.right)
            else:
                dfs(current_length + 1, 0, current_node.right)
                dfs(0, 1, current_node.left)

        dfs(0, 1, root.left)
        dfs(0, 0, root.right)

        return self.result
