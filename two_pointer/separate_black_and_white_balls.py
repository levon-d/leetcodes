class Solution:
    def minimumSteps(self, s: str) -> int:
        white_pointer = 0 
        result = 0 

        for i, char in enumerate(s): 
            if char == "0":
                result += (i - white_pointer)
                white_pointer += 1 
        
        return result
