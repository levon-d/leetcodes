class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        curr_min = 0 
        queue = deque()

        for i in range(len(grid)):
            broken = False
            for j in range(len(grid[0])): 
                if grid[i][j] == 2: 
                    queue.appendleft((i,j))

        while queue:
            
            prev_coordinates = []

            while queue: 
                prev_coordinates.append(queue.popleft())

            for prev_coordinate in prev_coordinates:
                up = (prev_coordinate[0]-1, prev_coordinate[1])
                down = (prev_coordinate[0]+1, prev_coordinate[1])
                left = (prev_coordinate[0], prev_coordinate[1]-1)
                right = (prev_coordinate[0], prev_coordinate[1]+1)

                adjacent = [left, right, up, down]

                for y,x in adjacent:
                    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid): 
                        continue 
                    if grid[y][x] == 1: 
                        queue.appendleft((y,x))
                        grid[y][x] = 2 
            if queue:
                curr_min += 1 
              
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == 1: 
                    return -1
                
        return curr_min
