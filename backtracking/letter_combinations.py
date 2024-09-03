class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digitsToLetters = {
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        } 

        result = [] 
        def backtrack(currentStr, digits, i):
            if i >= len(digits):
                result.append(currentStr)
                return 
            for char in digitsToLetters[int(digits[i])]: 
                stringWithNewChar = currentStr + char
                backtrack(stringWithNewChar, digits, i+1)

        backtrack("", digits, 0)
        return result 
