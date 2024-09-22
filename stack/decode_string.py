class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        newString = ""

        for char in s:
            if char == "]":
                current_char = stack.pop()
                current_string = current_char
                while stack[-1] != "[":
                    current_char = stack.pop()
                    if not current_char.isnumeric():
                        current_string = current_char + current_string
                stack.pop()
                repetitions = int(stack.pop())
                current_string = repetitions * current_string
                stack.append(current_string)
            else:
                if stack and char.isnumeric() and stack[-1].isnumeric():
                    stack[-1] += char
                else:
                    stack.append(char)

        return "".join(stack)
