"""
Given a string s, find the length of the longest 
substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        longest = 0
        l = 0 
        current_chars = set()

        for r in range(len(s)):
            while s[r] in current_chars:
                current_chars.remove(s[l])
                l+=1 

            current_chars.add(s[r])
            longest = max(longest, r-l+1)
            
        return longest            
