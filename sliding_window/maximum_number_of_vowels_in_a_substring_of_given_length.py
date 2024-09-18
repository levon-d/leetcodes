class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])

        l = 0 
        r = k
        currentVowels = len([char for char in s[:k] if char in vowels])
        maxVowels = currentVowels 

        for r in range(k, len(s)):
            if s[l] in vowels:
                currentVowels -= 1 
            if s[r] in vowels:
                currentVowels += 1 
            maxVowels = max(currentVowels, maxVowels)
            l+=1 

        return maxVowels
