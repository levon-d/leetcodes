class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        num_of_steps = 0 

        queue = deque([tuple(entrance)])
        visited = set([tuple(entrance)])
        while queue:
            current_positions = [] 

            while queue: 
                current_positions.append(tuple(queue.popleft()))

            for position in current_positions: 
                left = (position[0], position[1]-1)
                right = (position[0], position[1]+1)
                up = (position[0]-1, position[1])
                down = (position[0]+1, position[1])

                adjacents = [left, right, up, down]

                for (y,x) in adjacents: 
                    if y < 0 or x < 0 or y >= len(maze) or x >= len(maze[0]):
                        continue 
                    
                    if maze[y][x] == "." and not (y,x) in visited: 
                        if (y == len(maze) - 1 or y == 0 or x == len(maze[0]) - 1 or x == 0): 
                            return num_of_steps + 1 
                        queue.appendleft([y,x])
                        visited.add((y,x))
        
            num_of_steps += 1 
        
        return -1 
