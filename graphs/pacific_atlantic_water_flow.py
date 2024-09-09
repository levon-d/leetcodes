class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, previous_height):
            if (
                (r, c) in visited
                or r < 0
                or r == rows
                or c < 0
                or c == cols
                or previous_height > heights[r][c]
            ):
                return
            visited.add((r,c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for i in range(cols):
            dfs(0, i, pacific, heights[0][i])
            dfs(rows - 1, i, atlantic, heights[rows - 1][i])

        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols - 1, atlantic, heights[i][cols - 1])

        final = []

        for coordinates in pacific:
            if coordinates in atlantic:
                final.append(coordinates)

        return final 
