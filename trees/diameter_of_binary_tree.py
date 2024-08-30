class Solution:

    def __init__(self):
        self.maxDiameter = 0

    def depth(self, node): 
        if node == None:
            return 0 

        left = self.depth(node.left)
        right = self.depth(node.right)
        self.maxDiameter = max(left+right, self.maxDiameter)
        return 1+max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.maxDiameter
