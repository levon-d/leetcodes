class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node: 
                return 0 

            left, right = dfs(node.left), dfs(node.right)

            if abs(left-right) > 1 or left == -1 or right == -1:
                return -1 
            
            return 1+max(right, left)
        return dfs(root) != -1
        
