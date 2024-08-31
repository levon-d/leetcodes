class Solution:

    def match(self, t1, t2):
        if not t1 or not t2:
            return t1 == t2
        
        return t1.val == t2.val and self.match(t1.left, t2.left) and self.match(t1.right, t2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False 
        if self.match(root, subRoot):
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
