class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def backtrack(openNumber, closedNumber): 
            if openNumber == n and closedNumber == n:
                result.append("".join(stack))
                return

            if openNumber < n:
                stack.append('(')
                backtrack(openNumber+1, closedNumber)
                stack.pop()

            if closedNumber < openNumber:
                stack.append(')')
                backtrack(openNumber, closedNumber+1)
                stack.pop()

        backtrack(0,0)
        return result
