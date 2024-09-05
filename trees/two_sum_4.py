class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        visited = set()
        current = root 
        stack = []
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left 
            
            current = stack.pop()
            if (k-current.val) in visited:
                return True 
            visited.add(current.val)
            
            current = current.right 
        
        return False

