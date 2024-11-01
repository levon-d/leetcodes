class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        current_char = None 
        current_char_count = 0
        result = ""

        for char in s: 
            if char == current_char: 
                current_char_count += 1 
            
            else: 
                current_char_count = 1 
                current_char = char 
            
            if current_char_count < 3: 
                result += char 
        
        return result 

            
