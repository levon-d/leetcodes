class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return len([word for word in words if all(char in allowed for char in word)])
