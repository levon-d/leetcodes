class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        binary_start = bin(start)[2:]
        binary_goal = bin(goal)[2:]
        
        if len(binary_goal) > len(binary_start):
            binary_start = "0"*(len(binary_goal)-len(binary_start)) + binary_start 

        elif len(binary_start) > len(binary_goal):
            binary_goal = "0"*(len(binary_start)-len(binary_goal)) + binary_goal
        
        switches = 0
        for i in range(len(binary_goal)): 
            if binary_goal[i] != binary_start[i]:
                switches +=1 
        
        return switches
