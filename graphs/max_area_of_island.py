from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0 
        visited = set()

        def bfs(position): 
            currentArea = 0
            queue = deque([position])
            visited.add(position)
            while queue: 
                currentPosition = queue.popleft()
                
                # up
                if currentPosition[0] > 0 and grid[currentPosition[0]-1][currentPosition[1]] and (currentPosition[0]-1,currentPosition[1]) not in visited:
                    queue.append((currentPosition[0]-1,currentPosition[1]))
                    visited.add((currentPosition[0]-1,currentPosition[1]))
                
                # down
                if currentPosition[0] < len(grid)-1 and grid[currentPosition[0]+1][currentPosition[1]] and (currentPosition[0]+1,currentPosition[1]) not in visited:
                    queue.append((currentPosition[0]+1,currentPosition[1]))
                    visited.add((currentPosition[0]+1,currentPosition[1]))

                # left
                if currentPosition[1] > 0 and grid[currentPosition[0]][currentPosition[1]-1] and (currentPosition[0], currentPosition[1]-1) not in visited:
                    queue.append((currentPosition[0],currentPosition[1]-1))
                    visited.add((currentPosition[0],currentPosition[1]-1))
                
                # right
                if currentPosition[1] < len(grid[0])-1 and grid[currentPosition[0]][currentPosition[1]+1] and (currentPosition[0], currentPosition[1]+1) not in visited:
                    queue.append((currentPosition[0], currentPosition[1]+1))
                    visited.add((currentPosition[0], currentPosition[1]+1))
                
                currentArea+=1         
                # print(queue)
                # print(currentArea)
            return currentArea
        
        for i in range(len(grid)):
            for j in range(len(grid[i])): 
                if not grid[i][j] or (i,j) in visited:
                    continue 
                maxArea = max(bfs((i,j)), maxArea) 

        return maxArea
