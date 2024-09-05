class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        i = 0  
        j = 0  
        
        while j < len(haystack):
            if haystack[j] == needle[i]:
                i += 1
                j += 1
                
                if i == len(needle):
                    return j - i 
                
            else:
                j = j - i + 1 
                i = 0  
                
        return -1  
