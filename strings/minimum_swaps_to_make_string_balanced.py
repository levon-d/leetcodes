class Solution:
    def minSwaps(self, s: str) -> int:
        extra_closes, max_close = 0, 0 

        for char in s: 
            if char == "[":
                extra_closes -= 1 
            else:
                extra_closes += 1 
            max_close = max(extra_closes, max_close)
        
        return (max_close + 1) // 2
