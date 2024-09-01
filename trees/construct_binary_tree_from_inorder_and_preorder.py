class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None 
        
        root = TreeNode(val=preorder[0])

        index_of_root = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:index_of_root+1], inorder[:index_of_root])
        root.right = self.buildTree(preorder[index_of_root+1:], inorder[index_of_root+1:])


        return root 

