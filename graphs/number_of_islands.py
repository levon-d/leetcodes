class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        currentIsland = 0 

        def dfs(position): 
            if grid[position[0]][position[1]] != '1' or (position[0], position[1]) in visited:
                return 
            visited.add(position)
            if position[0] < len(grid)-1:
                dfs((position[0]+1, position[1]))
            if position[0] > 0:
                dfs((position[0]-1, position[1]))

            if position[1] < len(grid[0])-1:
                dfs((position[0], position[1]+1))
            if position[1] > 0:
                dfs((position[0], position[1]-1))
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0' or (i,j) in visited:
                    continue 
                
                dfs((i,j))
                currentIsland+=1 
        

        return currentIsland
