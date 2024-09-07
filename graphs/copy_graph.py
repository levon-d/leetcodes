"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']: 
        if not node:
            return None

        oldToNewNodeMapping = {} 

        def dfs(originNode): 
            if originNode in oldToNewNodeMapping:
                return oldToNewNodeMapping[originNode]
            
            copiedNode = Node(val=originNode.val)
            oldToNewNodeMapping[originNode] = copiedNode

            for neighbor in originNode.neighbors:
                copiedNode.neighbors.append(dfs(neighbor))

            return copiedNode 
        
        dfs(node)
        return oldToNewNodeMapping[node]

