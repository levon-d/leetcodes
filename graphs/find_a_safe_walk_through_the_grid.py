from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        queue = deque([(0,0,health - grid[0][0])])

        visited = set([(0,0,health - grid[0][0])])

        while queue: 
            row, col, current_health = queue.popleft()

            if (row, col) == (len(grid)-1, len(grid[0])-1):
                return True 
            
            left = (row, col-1)
            right = (row, col+1)
            up = (row-1, col)
            down = (row+1, col)

            if left[0] >= 0 and left[0] < len(grid) and left[1] >= 0 and left[1] < len(grid[0]): 
                updated_health = current_health - grid[left[0]][left[1]]
                if updated_health >= 1 and (left[0], left[1], updated_health) not in visited:
                    visited.add((left[0], left[1], updated_health))
                    queue.append((left[0],left[1],updated_health))
                    
            if right[0] >= 0 and right[0] < len(grid) and right[1] >= 0 and right[1] < len(grid[0]): 
                updated_health = current_health - grid[right[0]][right[1]]
                if updated_health >= 1 and (right[0], right[1], updated_health) not in visited:
                    visited.add((right[0], right[1], updated_health))
                    queue.append((right[0],right[1],updated_health))
                    

            if up[0] >= 0 and up[0] < len(grid) and up[1] >= 0 and up[1] < len(grid[0]): 
                updated_health = current_health - grid[up[0]][up[1]]
                if updated_health >= 1 and (up[0], up[1], updated_health) not in visited:
                    visited.add((up[0], up[1], updated_health))
                    queue.append((up[0],up[1],updated_health))
                    
            
            if down[0] >= 0 and down[0] < len(grid) and down[1] >= 0 and down[1] < len(grid[0]): 
                updated_health = current_health - grid[down[0]][down[1]]
                if updated_health >= 1 and (down[0], down[1], updated_health) not in visited:
                    visited.add((down[0], down[1], updated_health))
                    queue.append((down[0],down[1],updated_health))
                
        return False
