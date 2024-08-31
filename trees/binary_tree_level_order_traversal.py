from collections import deque 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        visited = []
        while queue:
            current_row = [] 
            for _ in range(len(queue)):
                node = queue.popleft()
                current_row.append(node.val)

                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            visited.append(current_row)
        return visited

