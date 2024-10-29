class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            dp[i][0] = 1 
        
        max_moves = 0 

        for j in range(1, len(grid[0])):
            for i in range(len(grid)): 
                if grid[i][j] > grid[i][j-1] and dp[i][j-1] > 0: 
                    dp[i][j] = max(dp[i][j], dp[i][j-1]+1)
                
                if i-1 >= 0 and grid[i][j] > grid[i-1][j-1] and dp[i-1][j-1] > 0: 
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
                
                if i+1 < len(grid) and grid[i][j] > grid[i+1][j-1] and dp[i+1][j-1] > 0:
                    dp[i][j] = max(dp[i][j], dp[i+1][j-1] + 1)
                
                max_moves = max(max_moves, dp[i][j]-1)
        
        return max_moves
