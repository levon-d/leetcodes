# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = []
        leafs2 = []
        def dfs(current_node, leafs):
            if not current_node:
                return

            if not current_node.left and not current_node.right:
                leafs.append(current_node.val)
                return 
            
            dfs(current_node.left, leafs)
            dfs(current_node.right, leafs)

        dfs(root1, leafs1)
        dfs(root2, leafs2)
        return leafs1 == leafs2
