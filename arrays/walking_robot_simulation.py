from enum import Enum

class Direction(Enum):
    NORTH = "NORTH"
    WEST = "WEST"
    EAST = "EAST"
    SOUTH = "SOUTH"

class Solution:

    def rotate(self, command, currentDirection): 
        newDirection = currentDirection
        match currentDirection:
            case Direction.NORTH:
                newDirection = Direction.EAST if command == -1 else Direction.WEST
            case Direction.EAST:
                newDirection = Direction.SOUTH if command == -1 else Direction.NORTH
            case Direction.SOUTH:
                newDirection = Direction.WEST if command == -1 else Direction.EAST
            case Direction.WEST:
                newDirection = Direction.NORTH if command == -1 else Direction.SOUTH
        return newDirection

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        currentPosition = [0,0]
        currentDirection = Direction.NORTH
        furthestDistance = 0
        obstacle_set = set()
        for obstacle in obstacles:
            obstacle_set.add(tuple(obstacle))
            
        obstacles = obstacle_set
        for command in commands: 
            if command < 0:
                currentDirection = self.rotate(command, currentDirection)
                continue 
            newPosition = copy.deepcopy(currentPosition)
            for i in range(command): 
                match currentDirection:
                    case Direction.NORTH:
                        newPosition[1]+=1 
                        if tuple(newPosition) in obstacles:
                            newPosition[1]-=1
                            break
                    case Direction.SOUTH:
                        newPosition[1]-=1 
                        if tuple(newPosition) in obstacles:
                            newPosition[1]+=1
                            break
                    case Direction.WEST:
                        newPosition[0]-=1 
                        if tuple(newPosition) in obstacles:
                            newPosition[0]+=1
                            break
                    case Direction.EAST:
                        newPosition[0]+=1 
                        if tuple(newPosition) in obstacles:
                            newPosition[0]-=1
                            break
            currentPosition = newPosition
            currentDistance = (currentPosition[0]**2) + (currentPosition[1]**2)
            furthestDistance = max(furthestDistance, currentDistance)
        
        return furthestDistance
        
                    
            

